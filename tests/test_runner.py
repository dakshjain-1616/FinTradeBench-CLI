"""Tests for runner.py"""

import subprocess
import sys
import pytest
from unittest.mock import patch, MagicMock

from fintradebench.runner import BenchmarkRunner
from fintradebench.dataset import QUESTIONS


SAMPLE_QUESTIONS = QUESTIONS[:5]


def test_runner_dry_run():
    """BenchmarkRunner.run(dry_run=True) returns results without API call."""
    runner = BenchmarkRunner(model="test/model")

    # Ensure no real API calls are made by patching _call_model
    with patch.object(runner, "_call_model") as mock_call:
        results = runner.run(questions=SAMPLE_QUESTIONS, dry_run=True)
        mock_call.assert_not_called()

    assert len(results) == len(SAMPLE_QUESTIONS)
    for r in results:
        assert "id" in r
        assert "category" in r
        assert "score" in r
        assert "answer" in r
        assert isinstance(r["score"], float)
        assert 0.0 <= r["score"] <= 1.0


def test_runner_dry_run_no_api_key():
    """dry_run does not require OPENROUTER_API_KEY."""
    runner = BenchmarkRunner(model="test/model", api_key=None)
    results = runner.run(questions=SAMPLE_QUESTIONS[:2], dry_run=True)
    assert len(results) == 2


def test_runner_dry_run_all_questions():
    """Full dry_run returns results for every question in the dataset."""
    runner = BenchmarkRunner(model="test/dry-run-full")
    results = runner.run(dry_run=True)
    assert len(results) == len(QUESTIONS)


def test_runner_run_full_dry_run():
    """run_full(dry_run=True) returns (results, total_score, category_scores)."""
    runner = BenchmarkRunner(model="test/model")
    results, total_score, category_scores = runner.run_full(dry_run=True)
    assert isinstance(results, list)
    assert isinstance(total_score, float)
    assert isinstance(category_scores, dict)
    assert 0.0 <= total_score <= 100.0
    assert len(category_scores) > 0


def test_runner_result_schema():
    """Each result contains required fields."""
    runner = BenchmarkRunner(model="test/model")
    results = runner.run(questions=SAMPLE_QUESTIONS[:3], dry_run=True)
    required = {"id", "category", "question", "answer", "reference_answer", "keywords", "score", "keywords_matched"}
    for r in results:
        for field in required:
            assert field in r, f"Missing field '{field}' in result: {r}"


def test_cli_leaderboard_flag(tmp_path):
    """--leaderboard flag reads reports dir and prints table (integration test)."""
    import json
    from pathlib import Path

    # Create a fake report file
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir()
    report = {
        "model": "test/leaderboard-model",
        "timestamp": "20240101T120000Z",
        "total_score": 65.5,
        "category_scores": {"market_analysis": 0.655},
        "results": [],
    }
    (reports_dir / "test_leaderboard-model_20240101T120000Z.json").write_text(
        json.dumps(report)
    )

    # Run benchmark.py --leaderboard with REPORTS_DIR patched
    result = subprocess.run(
        [
            sys.executable, "-c",
            f"""
import sys
sys.path.insert(0, '.')
from fintradebench import reporter
from pathlib import Path
reporter.REPORTS_DIR = Path(r'{reports_dir}')
reports = reporter.load_all_reports(reporter.REPORTS_DIR)
assert len(reports) == 1, f'Expected 1 report, got {{len(reports)}}'
reporter.print_leaderboard(reports)
print('LEADERBOARD_OK')
"""
        ],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent.parent),
    )
    assert result.returncode == 0, f"Process failed: {result.stderr}"
    assert "LEADERBOARD_OK" in result.stdout
