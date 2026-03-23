#!/usr/bin/env python3
"""
demo.py — Showcases all FinTradeBench features in a dry-run (no API key needed).
Completes in under 30 seconds.

Demonstrates:
  1. 5-question dry-run benchmark with rich terminal table
  2. Side-by-side model comparison table (mock data)
  3. HTML report generation
"""

from __future__ import annotations

from rich.console import Console

from fintradebench.dataset import QUESTIONS
from fintradebench.runner import BenchmarkRunner, DEFAULT_MODEL
from fintradebench.reporter import (
    build_report,
    save_report,
    save_html_report,
    print_results_table,
    print_comparison_table,
    REPORTS_DIR,
)
from fintradebench.scorer import compute_category_scores, compute_overall_score

console = Console()


_SEP = "━" * 49


def main() -> None:
    console.print(f"\n[bold blue]{_SEP}[/bold blue]")
    console.print("  [bold]📈 FinTradeBench Demo[/bold]  — Dry Run (no API key)")
    console.print(f"[bold blue]{_SEP}[/bold blue]\n")

    # ── 1. 5-question dry-run benchmark ──────────────────────────────────────
    console.print("[bold]1 / 3  Running 5-question dry-run benchmark…[/bold]")

    # One question from each category for a balanced demo
    categories_seen: set[str] = set()
    sample_questions = []
    for q in QUESTIONS:
        if q["category"] not in categories_seen:
            sample_questions.append(q)
            categories_seen.add(q["category"])
        if len(sample_questions) == 5:
            break

    model = f"demo/{DEFAULT_MODEL}"
    runner = BenchmarkRunner(model=model)
    results = runner.run(questions=sample_questions, dry_run=True)

    category_scores = compute_category_scores(results)
    total_score = compute_overall_score(results)

    report = build_report(
        model=model,
        results=results,
        total_score=total_score,
        category_scores=category_scores,
    )

    saved_path = save_report(report, REPORTS_DIR)
    print_results_table(report, console=console)
    console.print(f"[dim]JSON report saved → {saved_path}[/dim]")

    # ── 2. HTML report ────────────────────────────────────────────────────────
    console.print("\n[bold]2 / 3  Generating HTML report…[/bold]")
    html_path = save_html_report(report, REPORTS_DIR)
    console.print(f"[dim]HTML report saved → {html_path}[/dim]")

    # ── 3. Side-by-side comparison table (mock reports) ──────────────────────
    console.print("\n[bold]3 / 3  Showing comparison table (mock reports)…[/bold]")

    mock_alpha = build_report(
        model="demo/model-alpha",
        results=results,
        total_score=total_score,
        category_scores=category_scores,
    )
    # Slightly tweak scores to make the comparison table interesting
    mock_beta_scores = {cat: min(1.0, s + 0.15) for cat, s in category_scores.items()}
    mock_beta = build_report(
        model="demo/model-beta",
        results=results,
        total_score=min(100.0, total_score + 10),
        category_scores=mock_beta_scores,
    )

    print_comparison_table([mock_alpha, mock_beta], console=console)

    # ── Summary ───────────────────────────────────────────────────────────────
    console.print(f"\n[bold blue]{_SEP}[/bold blue]")
    console.print("  [bold green]✓ Demo complete![/bold green]")
    console.print(f"  JSON  → [dim]{saved_path}[/dim]")
    console.print(f"  HTML  → [dim]{html_path}[/dim]")
    console.print(
        "  Run [bold]python benchmark.py --model openai/gpt-4o[/bold] "
        "for a real benchmark"
    )
    console.print("  Built by [bold]NEO[/bold] · heyneo.so")
    console.print(f"[bold blue]{_SEP}[/bold blue]\n")


if __name__ == "__main__":
    main()
