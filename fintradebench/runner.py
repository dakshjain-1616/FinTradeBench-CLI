"""
BenchmarkRunner — orchestrates calling the LLM and scoring answers.
"""

from __future__ import annotations

import os
import random
import time
from typing import Any

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from .dataset import QUESTIONS
from .scorer import score_answer, compute_category_scores, compute_overall_score

DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "dry-run-model")

# Dry-run mock response template — cycles through a variety of "reasonable" answers
DRY_RUN_RESPONSES = [
    (
        "This represents a premium valuation with higher growth expectations. "
        "The market assigns higher earnings multiple due to anticipated future earnings growth. "
        "Investors expect strong momentum and superior performance versus peers."
    ),
    (
        "The golden cross is a bullish moving average crossover signal that indicates momentum "
        "shift. When the 50-day crosses above the 200-day, traders interpret it as a buy signal "
        "for upward trend continuation."
    ),
    (
        "Declining volume during a price downtrend indicates selling pressure is weakening. "
        "The momentum of the downtrend is fading, suggesting possible reversal or stabilization."
    ),
    (
        "A P/B ratio below 1.0 means the stock trades below its book value and net assets. "
        "Often seen in banking and financial sectors, it can signal undervaluation or distress."
    ),
    (
        "The VIX measures implied volatility and market fear. High VIX above 30 signals panic "
        "and uncertainty. Investors use it as a contrarian indicator — extreme fear may be a "
        "buying opportunity while low VIX warns of complacency."
    ),
]


class BenchmarkRunner:
    """Runs the full benchmark suite against a specified model."""

    def __init__(self, model: str, api_key: str | None = None):
        self.model = model
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY", "")
        self.console = Console()

    def _get_mock_response(self, question_index: int) -> str:
        """Return a cycling mock response for dry-run mode."""
        return DRY_RUN_RESPONSES[question_index % len(DRY_RUN_RESPONSES)]

    def _call_confidence(self, answer: str) -> float:
        """Make a second LLM call to rate confidence in the answer (1–5)."""
        try:
            from openai import OpenAI

            client = OpenAI(
                base_url=os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
                api_key=self.api_key,
            )
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Given this answer: {answer}\n\n"
                            "Rate your confidence in the above answer from 1 (guessing) "
                            "to 5 (certain). Reply with only the number."
                        ),
                    }
                ],
                max_tokens=10,
                temperature=0.0,
            )
            text = (response.choices[0].message.content or "3").strip()
            value = float(text)
            return max(1.0, min(5.0, value))
        except Exception:
            return 3.0

    def _call_model(self, question: str) -> str:
        """Call the LLM via OpenRouter and return the answer string."""
        try:
            from openai import OpenAI

            client = OpenAI(
                base_url=os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
                api_key=self.api_key,
            )
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a financial expert. Answer the following financial "
                            "reasoning question concisely and accurately. Provide a clear, "
                            "direct answer demonstrating your financial knowledge."
                        ),
                    },
                    {"role": "user", "content": question},
                ],
                max_tokens=400,
                temperature=0.1,
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            self.console.print(f"[red]API call failed: {e}[/red]")
            return ""

    def run(
        self,
        questions: list[dict] | None = None,
        dry_run: bool = False,
    ) -> list[dict[str, Any]]:
        """
        Run the benchmark.

        Args:
            questions: subset of questions to run (defaults to full dataset)
            dry_run: if True, use mock responses instead of real API calls

        Returns:
            List of per-question result dicts.
        """
        questions = questions if questions is not None else QUESTIONS
        results: list[dict[str, Any]] = []

        mode_label = "[yellow]DRY RUN[/yellow]" if dry_run else f"[cyan]{self.model}[/cyan]"
        self.console.print(f"\nRunning FinTradeBench on {mode_label}")
        self.console.print(f"Questions: {len(questions)}\n")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=self.console,
            transient=False,
        ) as progress:
            task = progress.add_task("Benchmarking...", total=len(questions))

            for idx, q in enumerate(questions):
                progress.update(
                    task,
                    description=f"[{q['id']}] {q['category']}",
                )

                if dry_run:
                    answer = self._get_mock_response(idx)
                    confidence = random.uniform(3.0, 5.0)
                    time_taken = random.uniform(0.1, 0.5)
                else:
                    t0 = time.time()
                    answer = self._call_model(q["question"])
                    time_taken = time.time() - t0
                    confidence = self._call_confidence(answer)
                    # Small delay to respect rate limits
                    time.sleep(0.5)

                score = score_answer(answer, q)

                # Compute keyword details for display
                kw_total = len(q.get("keywords", []))
                kw_matched = sum(
                    1 for kw in q.get("keywords", []) if kw.lower() in answer.lower()
                )

                results.append(
                    {
                        "id": q["id"],
                        "category": q["category"],
                        "question": q["question"],
                        "answer": answer,
                        "reference_answer": q["reference_answer"],
                        "keywords": q.get("keywords", []),
                        "score": score,
                        "keywords_matched": f"{kw_matched}/{kw_total}",
                        "confidence": confidence,
                        "time_taken_s": time_taken,
                    }
                )
                progress.advance(task)

        return results

    def run_full(
        self, dry_run: bool = False, category: str | None = None, max_questions: int = 0
    ) -> tuple[list[dict], float, dict[str, float]]:
        """
        Run the full benchmark and return (results, total_score, category_scores).

        Args:
            dry_run: if True, use mock responses instead of real API calls
            category: if set, only run questions from this category
            max_questions: if > 0, limit the number of questions run
        """
        from .dataset import get_questions_by_category

        questions = get_questions_by_category(category) if category else None
        if max_questions > 0:
            src = questions if questions is not None else QUESTIONS
            questions = src[:max_questions]
        results = self.run(questions=questions, dry_run=dry_run)
        category_scores = compute_category_scores(results)
        total_score = compute_overall_score(results)
        return results, total_score, category_scores
