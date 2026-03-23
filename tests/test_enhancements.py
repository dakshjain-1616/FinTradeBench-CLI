"""Tests for enhancement features (Features 1–7)."""

from __future__ import annotations

import pytest
from io import StringIO
from pathlib import Path

from rich.console import Console


# ── Feature 6: Dataset size ────────────────────────────────────────────────────

def test_dataset_min_size():
    """Dataset must have at least 65 questions after new additions."""
    from fintradebench.dataset import QUESTIONS
    assert len(QUESTIONS) >= 65, f"Expected >=65 questions, got {len(QUESTIONS)}"


# ── Feature 1: Comparison table ───────────────────────────────────────────────

def test_comparison_table():
    """print_comparison_table runs without error given 2 mock reports."""
    from fintradebench.reporter import print_comparison_table

    mock_reports = [
        {
            "model": "model/alpha",
            "total_score": 72.0,
            "category_scores": {
                "market_analysis": 0.72,
                "risk_assessment": 0.65,
            },
        },
        {
            "model": "model/beta",
            "total_score": 68.0,
            "category_scores": {
                "market_analysis": 0.60,
                "risk_assessment": 0.78,
            },
        },
    ]

    # Should not raise; capture output to avoid polluting test output
    console = Console(file=StringIO(), highlight=False)
    print_comparison_table(mock_reports, console=console)


# ── Feature 2: Confidence scoring ─────────────────────────────────────────────

def test_confidence_in_dry_run():
    """Dry-run results include a confidence field between 1 and 5."""
    from fintradebench.runner import BenchmarkRunner
    from fintradebench.dataset import QUESTIONS

    runner = BenchmarkRunner(model="test/model")
    results = runner.run(questions=QUESTIONS[:5], dry_run=True)

    for r in results:
        assert "confidence" in r, f"Missing 'confidence' in result: {r}"
        assert 1.0 <= r["confidence"] <= 5.0, (
            f"confidence={r['confidence']} out of [1, 5]"
        )


# ── Feature 3: Category filter ────────────────────────────────────────────────

def test_category_filter():
    """Runner with category='market_analysis' returns only MA questions."""
    from fintradebench.runner import BenchmarkRunner

    runner = BenchmarkRunner(model="test/model")
    results, _, category_scores = runner.run_full(dry_run=True, category="market_analysis")

    assert len(results) > 0, "Expected at least one result for market_analysis"
    for r in results:
        assert r["category"] == "market_analysis", (
            f"Got category '{r['category']}' when filtering by market_analysis"
        )
    assert list(category_scores.keys()) == ["market_analysis"]


# ── Feature 4: HTML report ────────────────────────────────────────────────────

def test_html_report_generated(tmp_path):
    """save_html_report creates a .html file containing the model name."""
    from fintradebench.reporter import save_html_report

    report = {
        "model": "test/html-model",
        "timestamp": "20240101T120000Z",
        "total_score": 55.5,
        "avg_confidence": 3.8,
        "avg_time_s": 0.25,
        "category_scores": {"market_analysis": 0.55, "risk_assessment": 0.60},
        "results": [
            {
                "id": "MA001",
                "category": "market_analysis",
                "score": 0.8,
                "confidence": 4.0,
                "time_taken_s": 0.3,
                "answer": "This is a test answer for the HTML report.",
            }
        ],
    }

    html_path = save_html_report(report, reports_dir=tmp_path)
    path = Path(html_path)

    assert path.exists(), f"HTML file not created at {html_path}"
    assert path.suffix == ".html"

    content = path.read_text(encoding="utf-8")
    assert "test/html-model" in content, "Model name not found in HTML report"


# ── Feature 5: Timed answers ──────────────────────────────────────────────────

def test_timed_answers_dry_run():
    """Dry-run results include time_taken_s > 0 for each question."""
    from fintradebench.runner import BenchmarkRunner
    from fintradebench.dataset import QUESTIONS

    runner = BenchmarkRunner(model="test/model")
    results = runner.run(questions=QUESTIONS[:5], dry_run=True)

    for r in results:
        assert "time_taken_s" in r, f"Missing 'time_taken_s' in result: {r}"
        assert r["time_taken_s"] > 0, (
            f"time_taken_s={r['time_taken_s']} should be > 0"
        )


def test_avg_time_in_report():
    """build_report includes avg_time_s key in the returned dict."""
    from fintradebench.reporter import build_report

    results = [
        {"id": "MA001", "category": "market_analysis", "score": 0.7,
         "confidence": 4.0, "time_taken_s": 0.3},
        {"id": "MA002", "category": "market_analysis", "score": 0.5,
         "confidence": 3.5, "time_taken_s": 0.2},
    ]
    report = build_report(
        model="test/model",
        results=results,
        total_score=60.0,
        category_scores={"market_analysis": 0.6},
    )

    assert "avg_time_s" in report, "avg_time_s key missing from report"
    assert report["avg_time_s"] == pytest.approx(0.25, rel=1e-3)
    assert "avg_confidence" in report, "avg_confidence key missing from report"
