"""Tests for dataset.py"""

import pytest
from fintradebench.dataset import QUESTIONS, get_categories, get_questions_by_category


REQUIRED_CATEGORIES = {
    "market_analysis",
    "risk_assessment",
    "earnings_interpretation",
    "trading_strategy",
    "macro_economics",
}

REQUIRED_QUESTION_FIELDS = {"id", "category", "question", "reference_answer", "keywords"}


def test_dataset_size():
    """Dataset has >= 50 questions."""
    assert len(QUESTIONS) >= 50, f"Expected >= 50 questions, got {len(QUESTIONS)}"


def test_dataset_categories():
    """All 5 categories present; each has >= 5 questions."""
    categories = get_categories()
    category_set = set(categories)

    for required in REQUIRED_CATEGORIES:
        assert required in category_set, f"Missing category: {required}"

    for cat in REQUIRED_CATEGORIES:
        questions = get_questions_by_category(cat)
        assert len(questions) >= 5, (
            f"Category '{cat}' has only {len(questions)} questions, need >= 5"
        )


def test_question_schema():
    """Every question has: id, category, question, reference_answer, keywords."""
    for q in QUESTIONS:
        for field in REQUIRED_QUESTION_FIELDS:
            assert field in q, f"Question {q.get('id', '?')} missing field: {field}"
        # id and category must be non-empty strings
        assert isinstance(q["id"], str) and q["id"], f"Empty id in question: {q}"
        assert isinstance(q["category"], str) and q["category"], f"Empty category in: {q['id']}"
        # question and reference_answer must be non-empty strings
        assert isinstance(q["question"], str) and q["question"], f"Empty question in: {q['id']}"
        assert isinstance(q["reference_answer"], str) and q["reference_answer"], (
            f"Empty reference_answer in: {q['id']}"
        )
        # keywords must be a non-empty list of strings
        assert isinstance(q["keywords"], list) and len(q["keywords"]) > 0, (
            f"Empty keywords in: {q['id']}"
        )
        for kw in q["keywords"]:
            assert isinstance(kw, str) and kw, f"Invalid keyword in {q['id']}: {kw!r}"
