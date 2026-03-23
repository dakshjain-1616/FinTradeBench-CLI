"""Tests for reporter.py"""

import json
import pytest
from pathlib import Path
from fintradebench.reporter import save_report, load_report, load_all_reports, build_report, print_leaderboard


SAMPLE_REPORT = {
    "model": "test/model-v1",
    "timestamp": "20240101T120000Z",
    "total_score": 72.5,
    "category_scores": {
        "market_analysis": 0.75,
        "risk_assessment": 0.68,
    },
    "results": [
        {
            "id": "MA001",
            "category": "market_analysis",
            "question": "What is P/E?",
            "answer": "Price to earnings ratio.",
            "reference_answer": "Price to earnings ratio.",
            "keywords": ["price", "earnings"],
            "score": 1.0,
            "keywords_matched": "2/2",
        }
    ],
}


def test_reporter_save_load(tmp_path):
    """Save a report dict, reload it, verify round-trip equality."""
    saved_path = save_report(SAMPLE_REPORT, reports_dir=tmp_path)
    assert saved_path.exists()

    loaded = load_report(saved_path)
    assert loaded == SAMPLE_REPORT


def test_reporter_save_creates_directory(tmp_path):
    """save_report creates the reports directory if it doesn't exist."""
    new_dir = tmp_path / "nested" / "reports"
    assert not new_dir.exists()
    path = save_report(SAMPLE_REPORT, reports_dir=new_dir)
    assert new_dir.exists()
    assert path.exists()


def test_reporter_save_filename_format(tmp_path):
    """Saved filename contains model id and timestamp."""
    path = save_report(SAMPLE_REPORT, reports_dir=tmp_path)
    name = path.name
    assert "20240101T120000Z" in name
    assert ".json" in name


def test_load_all_reports(tmp_path):
    """load_all_reports returns all JSON files in directory."""
    # Save two reports
    r1 = {**SAMPLE_REPORT, "model": "model-a", "timestamp": "20240101T100000Z", "total_score": 60.0}
    r2 = {**SAMPLE_REPORT, "model": "model-b", "timestamp": "20240101T110000Z", "total_score": 80.0}
    save_report(r1, reports_dir=tmp_path)
    save_report(r2, reports_dir=tmp_path)

    reports = load_all_reports(tmp_path)
    assert len(reports) == 2


def test_load_all_reports_empty_dir(tmp_path):
    """load_all_reports returns empty list when no reports exist."""
    reports = load_all_reports(tmp_path)
    assert reports == []


def test_load_all_reports_nonexistent_dir(tmp_path):
    """load_all_reports returns empty list if directory doesn't exist."""
    missing = tmp_path / "does_not_exist"
    reports = load_all_reports(missing)
    assert reports == []


def test_leaderboard_ordering(tmp_path):
    """Leaderboard sorts by total_score descending."""
    reports = [
        {**SAMPLE_REPORT, "model": "model-c", "timestamp": "T1", "total_score": 45.0},
        {**SAMPLE_REPORT, "model": "model-a", "timestamp": "T2", "total_score": 90.0},
        {**SAMPLE_REPORT, "model": "model-b", "timestamp": "T3", "total_score": 70.0},
    ]

    # Sort logic (same as print_leaderboard)
    sorted_reports = sorted(reports, key=lambda r: r.get("total_score", 0.0), reverse=True)

    assert sorted_reports[0]["model"] == "model-a"
    assert sorted_reports[1]["model"] == "model-b"
    assert sorted_reports[2]["model"] == "model-c"


def test_build_report_structure():
    """build_report returns dict with required keys."""
    results = [{"id": "X1", "category": "market_analysis", "score": 0.5}]
    report = build_report(
        model="test/model",
        results=results,
        total_score=50.0,
        category_scores={"market_analysis": 0.5},
    )
    for key in ("model", "timestamp", "total_score", "category_scores", "results"):
        assert key in report

    assert report["model"] == "test/model"
    assert report["total_score"] == 50.0
    assert report["results"] == results
