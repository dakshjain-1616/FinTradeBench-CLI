"""Tests for scorer.py"""

import pytest
from fintradebench.scorer import (
    score_exact_match,
    score_keyword_overlap,
    score_answer,
    compute_category_scores,
    compute_overall_score,
)


SAMPLE_QUESTION = {
    "id": "TEST001",
    "category": "market_analysis",
    "question": "What is a P/E ratio?",
    "reference_answer": "The price-to-earnings ratio divides stock price by earnings per share.",
    "keywords": ["price", "earnings", "ratio", "stock", "per share"],
}


def test_scorer_exact_match():
    """score=1.0 when answer matches reference exactly."""
    answer = SAMPLE_QUESTION["reference_answer"]
    score = score_answer(answer, SAMPLE_QUESTION)
    assert score == 1.0


def test_scorer_exact_match_case_insensitive():
    """Exact match is case-insensitive."""
    answer = SAMPLE_QUESTION["reference_answer"].upper()
    assert score_exact_match(answer, SAMPLE_QUESTION["reference_answer"]) == 1.0


def test_scorer_keyword_overlap():
    """Correct partial scoring based on keyword presence."""
    # Answer contains 3 of 5 keywords: "price", "earnings", "ratio"
    answer = "The price to earnings ratio is a valuation metric."
    score = score_keyword_overlap(answer, SAMPLE_QUESTION["keywords"])
    # "price" ✓, "earnings" ✓, "ratio" ✓, "stock" ✗, "per share" ✗ → 3/5 = 0.6
    assert score == pytest.approx(3 / 5, abs=0.01)


def test_scorer_keyword_overlap_all_present():
    """Score = 1.0 when all keywords are present."""
    answer = "The price to earnings ratio measures how stock is valued per share."
    score = score_keyword_overlap(answer, SAMPLE_QUESTION["keywords"])
    assert score == pytest.approx(1.0, abs=0.01)


def test_scorer_keyword_overlap_none_present():
    """Score = 0.0 when no keywords are present."""
    answer = "I have no idea."
    score = score_keyword_overlap(answer, SAMPLE_QUESTION["keywords"])
    assert score == pytest.approx(0.0, abs=0.01)


def test_scorer_empty_answer():
    """score=0.0 for blank answer."""
    for blank in ["", "   ", "\t\n"]:
        assert score_answer(blank, SAMPLE_QUESTION) == 0.0
    assert score_exact_match("", "anything") == 0.0
    assert score_keyword_overlap("", ["keyword"]) == 0.0


def test_scorer_partial_match_returns_float():
    """score_answer returns float between 0 and 1 for partial match."""
    answer = "The price to earnings metric."
    score = score_answer(answer, SAMPLE_QUESTION)
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0


def test_compute_category_scores():
    """compute_category_scores returns per-category averages."""
    results = [
        {"category": "market_analysis", "score": 0.8},
        {"category": "market_analysis", "score": 0.6},
        {"category": "risk_assessment", "score": 1.0},
    ]
    cats = compute_category_scores(results)
    assert cats["market_analysis"] == pytest.approx(0.7, abs=0.01)
    assert cats["risk_assessment"] == pytest.approx(1.0, abs=0.01)


def test_compute_overall_score():
    """compute_overall_score returns 0–100."""
    results = [{"score": 0.8}, {"score": 0.4}, {"score": 1.0}]
    score = compute_overall_score(results)
    assert score == pytest.approx(73.33, abs=0.1)


def test_compute_overall_score_empty():
    """compute_overall_score returns 0 for empty results."""
    assert compute_overall_score([]) == 0.0
