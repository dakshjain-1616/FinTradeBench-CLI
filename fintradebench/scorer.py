"""
Scoring logic for FinTradeBench.

Two scoring modes:
- exact_match: 1.0 if the answer matches the reference exactly (case-insensitive strip)
- keyword_overlap: fraction of expected keywords found in the answer
"""

from __future__ import annotations


def score_exact_match(answer: str, reference_answer: str) -> float:
    """Return 1.0 if answer matches reference exactly (case-insensitive), else 0.0."""
    if not answer or not answer.strip():
        return 0.0
    return 1.0 if answer.strip().lower() == reference_answer.strip().lower() else 0.0


def score_keyword_overlap(answer: str, keywords: list[str]) -> float:
    """
    Return fraction of keywords found in answer (case-insensitive).
    Returns 0.0 for empty answers or empty keyword lists.
    """
    if not answer or not answer.strip():
        return 0.0
    if not keywords:
        return 0.0
    answer_lower = answer.lower()
    matched = sum(1 for kw in keywords if kw.lower() in answer_lower)
    return matched / len(keywords)


def score_answer(answer: str, question: dict) -> float:
    """
    Score a single answer against the question's rubric.

    Strategy:
    - If exact match → 1.0
    - Otherwise → keyword overlap score
    Returns a float in [0.0, 1.0].
    """
    if not answer or not answer.strip():
        return 0.0

    exact = score_exact_match(answer, question["reference_answer"])
    if exact == 1.0:
        return 1.0

    return score_keyword_overlap(answer, question.get("keywords", []))


def compute_category_scores(results: list[dict]) -> dict[str, float]:
    """
    Given a list of per-question result dicts (each with 'category' and 'score'),
    return a dict mapping category → average score.
    """
    from collections import defaultdict

    category_scores: dict[str, list[float]] = defaultdict(list)
    for r in results:
        category_scores[r["category"]].append(r["score"])

    return {cat: sum(scores) / len(scores) for cat, scores in category_scores.items()}


def compute_overall_score(results: list[dict]) -> float:
    """Return overall score as 0–100 from per-question 0–1 scores."""
    if not results:
        return 0.0
    avg = sum(r["score"] for r in results) / len(results)
    return round(avg * 100, 2)
