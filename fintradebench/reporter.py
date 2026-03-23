"""
Report generation: save/load JSON reports and render ASCII tables.
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.table import Table
from rich import box

from .dataset import CATEGORY_DISPLAY_NAMES

REPORTS_DIR = Path(os.environ.get("REPORTS_DIR", "reports"))


def save_report(report: dict[str, Any], reports_dir: Path = REPORTS_DIR) -> Path:
    """Save a report dict to JSON. Returns the path written."""
    reports_dir.mkdir(parents=True, exist_ok=True)
    model_id = report["model"].replace("/", "_").replace(":", "_")
    timestamp = report["timestamp"]
    filename = f"{model_id}_{timestamp}.json"
    path = reports_dir / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    return path


def load_report(path: Path) -> dict[str, Any]:
    """Load and return a report dict from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_all_reports(reports_dir: Path = REPORTS_DIR) -> list[dict[str, Any]]:
    """Load all JSON report files from reports_dir."""
    if not reports_dir.exists():
        return []
    reports = []
    for p in sorted(reports_dir.glob("*.json")):
        try:
            reports.append(load_report(p))
        except (json.JSONDecodeError, OSError):
            pass
    return reports


def build_report(
    model: str,
    results: list[dict],
    total_score: float,
    category_scores: dict[str, float],
) -> dict[str, Any]:
    """Build a report dict from run results."""
    avg_confidence = 0.0
    avg_time_s = 0.0
    if results:
        avg_confidence = sum(r.get("confidence", 0.0) for r in results) / len(results)
        avg_time_s = sum(r.get("time_taken_s", 0.0) for r in results) / len(results)
    return {
        "model": model,
        "timestamp": datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"),
        "total_score": total_score,
        "category_scores": category_scores,
        "avg_confidence": avg_confidence,
        "avg_time_s": avg_time_s,
        "results": results,
    }


def print_results_table(report: dict[str, Any], console: Console | None = None) -> None:
    """Print a rich ASCII table summarising the benchmark results."""
    if console is None:
        console = Console()

    model = report["model"]
    total_score = report["total_score"]
    category_scores = report.get("category_scores", {})
    avg_confidence = report.get("avg_confidence", 0.0)
    avg_time_s = report.get("avg_time_s", 0.0)

    console.print(f"\n[bold cyan]FinTradeBench Results — {model}[/bold cyan]")
    console.print(f"[bold]Overall Score: {total_score:.1f} / 100[/bold]")
    console.print(
        f"Avg Confidence: {avg_confidence:.2f}/5.0  |  Avg Time: {avg_time_s:.2f}s\n"
    )

    # Category breakdown table
    cat_table = Table(title="Category Breakdown", box=box.ROUNDED)
    cat_table.add_column("Category", style="cyan", min_width=25)
    cat_table.add_column("Avg Score", justify="right", style="green")
    cat_table.add_column("Pct", justify="right")

    for cat, avg in sorted(category_scores.items()):
        display = CATEGORY_DISPLAY_NAMES.get(cat, cat)
        pct = f"{avg * 100:.1f}%"
        cat_table.add_row(display, f"{avg:.3f}", pct)

    console.print(cat_table)

    # Per-question table
    q_table = Table(title="Per-Question Results", box=box.SIMPLE_HEAVY)
    q_table.add_column("ID", style="dim", min_width=6)
    q_table.add_column("Category", min_width=20)
    q_table.add_column("Score", justify="right")
    q_table.add_column("Conf", justify="right")
    q_table.add_column("Time(s)", justify="right")
    q_table.add_column("Keywords matched", justify="right")

    for r in report.get("results", []):
        score = r.get("score", 0.0)
        color = "green" if score >= 0.7 else ("yellow" if score >= 0.4 else "red")
        conf = r.get("confidence", 0.0)
        time_s = r.get("time_taken_s", 0.0)
        q_table.add_row(
            r.get("id", ""),
            CATEGORY_DISPLAY_NAMES.get(r.get("category", ""), r.get("category", "")),
            f"[{color}]{score:.2f}[/{color}]",
            f"{conf:.1f}",
            f"{time_s:.2f}",
            r.get("keywords_matched", ""),
        )

    console.print(q_table)


def print_comparison_table(
    reports: list[dict[str, Any]], console: Console | None = None
) -> None:
    """Print a side-by-side comparison table for multiple model reports."""
    if console is None:
        console = Console()

    if not reports:
        console.print("[yellow]No reports to compare.[/yellow]")
        return

    # Collect all categories across all reports
    all_cats: set[str] = set()
    for r in reports:
        all_cats.update(r.get("category_scores", {}).keys())
    sorted_cats = sorted(all_cats)

    table = Table(title="Model Comparison", box=box.ROUNDED)
    table.add_column("Category", style="cyan", min_width=25)
    for r in reports:
        table.add_column(r.get("model", "unknown"), justify="right", min_width=12)

    for cat in sorted_cats:
        scores = [r.get("category_scores", {}).get(cat, 0.0) for r in reports]
        max_score = max(scores) if scores else 0.0
        row_values: list[str] = []
        for s in scores:
            color = "green" if s == max_score else "white"
            row_values.append(f"[{color}]{s:.3f}[/{color}]")
        display = CATEGORY_DISPLAY_NAMES.get(cat, cat)
        table.add_row(display, *row_values)

    # Overall row
    overall_scores = [r.get("total_score", 0.0) for r in reports]
    max_overall = max(overall_scores) if overall_scores else 0.0
    overall_values: list[str] = []
    for s in overall_scores:
        color = "green" if s == max_overall else "white"
        overall_values.append(f"[{color}]{s:.1f}[/{color}]")
    table.add_row("[bold]Overall[/bold]", *overall_values)

    console.print(table)


def save_html_report(report: dict[str, Any], reports_dir: Path = REPORTS_DIR) -> str:
    """Generate and save a self-contained HTML report. Returns the file path."""
    reports_dir.mkdir(parents=True, exist_ok=True)
    model_id = report["model"].replace("/", "_").replace(":", "_")
    timestamp = report["timestamp"]
    filename = f"{model_id}_{timestamp}.html"
    path = reports_dir / filename

    model = report["model"]
    total_score = report["total_score"]
    category_scores = report.get("category_scores", {})
    results = report.get("results", [])

    # Category bar chart rows
    cat_bars_html = ""
    for cat, score in sorted(category_scores.items()):
        display = CATEGORY_DISPLAY_NAMES.get(cat, cat)
        pct = score * 100
        cat_bars_html += (
            f'<div class="bar-row">'
            f'<div class="bar-label">{display}</div>'
            f'<div class="bar-track">'
            f'<div class="bar-fill" style="--bar-width:{pct:.1f}%">{pct:.1f}%</div>'
            f"</div></div>\n"
        )

    # Per-question accordion rows
    rows_html = ""
    for r in results:
        score = r.get("score", 0.0)
        conf = r.get("confidence", 0.0)
        time_s = r.get("time_taken_s", 0.0)
        cat_display = CATEGORY_DISPLAY_NAMES.get(r.get("category", ""), r.get("category", ""))
        question_txt = (r.get("question", "") or "").replace("<", "&lt;").replace(">", "&gt;")
        answer_txt = (r.get("answer", "") or "").replace("<", "&lt;").replace(">", "&gt;")
        ref_txt = (r.get("reference_answer", "") or "").replace("<", "&lt;").replace(">", "&gt;")
        score_class = "score-hi" if score >= 0.7 else ("score-mid" if score >= 0.4 else "score-lo")
        rows_html += (
            f'<details>'
            f'<summary>'
            f'<span class="acc-chevron">▶</span>'
            f'<span class="acc-id">{r.get("id", "")}</span>'
            f'<span class="acc-cat">{cat_display}</span>'
            f'<span class="acc-score {score_class}">{score:.2f}</span>'
            f'</summary>'
            f'<div class="acc-body">'
            f'<div class="acc-meta">'
            f'<span>Confidence: {conf:.1f}/5</span>'
            f'<span>Time: {time_s:.2f}s</span>'
            f'<span>Keywords: {r.get("keywords_matched", "")}</span>'
            f'</div>'
            f'<div class="acc-block"><label>Question</label><p>{question_txt}</p></div>'
            f'<div class="acc-block"><label>Model Answer</label>'
            f'<p class="answer">{answer_txt}</p></div>'
            f'<div class="acc-block"><label>Reference Answer</label>'
            f'<p class="reference">{ref_txt}</p></div>'
            f'</div>'
            f'</details>\n'
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FinTradeBench — {model}</title>
<style>
/* ── Reset & base ── */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #f4f6fb;
  color: #1a1a2e;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}}

/* ── Header ── */
header {{
  background: #1a1a2e;
  color: white;
  padding: 28px 40px 24px;
}}
header h1 {{
  font-size: 1.7rem;
  font-weight: 700;
  letter-spacing: -0.5px;
}}
header .subtitle {{
  color: #8892b0;
  font-size: 0.9rem;
  margin-top: 4px;
}}
header .score-badge {{
  display: inline-block;
  background: #4CAF50;
  color: white;
  font-size: 1.5rem;
  font-weight: 700;
  padding: 6px 18px;
  border-radius: 8px;
  margin-top: 14px;
}}

/* ── Main content ── */
main {{
  max-width: 1100px;
  width: 100%;
  margin: 32px auto;
  padding: 0 24px;
  flex: 1;
}}

/* ── Cards ── */
.card {{
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,.07);
  padding: 24px 28px;
  margin-bottom: 24px;
}}
.card h2 {{
  font-size: 1.05rem;
  font-weight: 600;
  color: #1a1a2e;
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 1px solid #e8ecf4;
}}

/* ── Meta grid ── */
.meta-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
}}
.meta-item {{
  background: #f0f4ff;
  border-radius: 6px;
  padding: 10px 14px;
}}
.meta-item .label {{
  font-size: 0.75rem;
  color: #5a6a8a;
  text-transform: uppercase;
  letter-spacing: .5px;
}}
.meta-item .value {{
  font-size: 1rem;
  font-weight: 600;
  color: #1a1a2e;
  margin-top: 2px;
}}

/* ── Bar chart (animated) ── */
@keyframes fillBar {{
  from {{ width: 0%; }}
  to   {{ width: var(--bar-width); }}
}}
.bar-row {{
  display: flex;
  align-items: center;
  margin: 8px 0;
}}
.bar-label {{
  width: 220px;
  font-size: 0.85rem;
  color: #334;
  flex-shrink: 0;
}}
.bar-track {{
  flex: 1;
  background: #e8ecf4;
  border-radius: 6px;
  height: 24px;
  overflow: hidden;
}}
.bar-fill {{
  background: linear-gradient(90deg, #4CAF50, #66bb6a);
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  height: 100%;
  border-radius: 6px;
  display: flex;
  align-items: center;
  padding-left: 8px;
  min-width: 40px;
  animation: fillBar 0.8s ease-out forwards;
  width: 0%;
}}

/* ── Accordion (per-question) ── */
details {{
  border: 1px solid #e8ecf4;
  border-radius: 6px;
  margin-bottom: 6px;
  overflow: hidden;
}}
details summary {{
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  cursor: pointer;
  user-select: none;
  background: #fafbff;
  list-style: none;
  font-size: 0.88rem;
}}
details summary::-webkit-details-marker {{ display: none; }}
details[open] summary {{ background: #f0f4ff; border-bottom: 1px solid #e8ecf4; }}
details summary:hover {{ background: #eef1fb; }}
.acc-id    {{ font-weight: 700; color: #1a1a2e; width: 60px; flex-shrink: 0; }}
.acc-cat   {{ color: #5a6a8a; width: 180px; flex-shrink: 0; font-size: 0.82rem; }}
.acc-score {{ margin-left: auto; font-weight: 700; }}
.score-hi  {{ color: #2e7d32; }}
.score-mid {{ color: #f57c00; }}
.score-lo  {{ color: #c62828; }}
.acc-chevron {{ color: #aab; transition: transform .2s; }}
details[open] .acc-chevron {{ transform: rotate(90deg); }}
.acc-body  {{ padding: 14px 16px; font-size: 0.84rem; display: grid; gap: 10px; }}
.acc-block label {{ font-size: 0.72rem; text-transform: uppercase; letter-spacing: .5px;
                    color: #8892b0; display: block; margin-bottom: 3px; }}
.acc-block p  {{ line-height: 1.5; color: #223; }}
.acc-block .answer {{ background: #f8faff; border-left: 3px solid #4CAF50;
                      padding: 8px 10px; border-radius: 0 4px 4px 0; }}
.acc-block .reference {{ background: #f8f8f8; border-left: 3px solid #90a4ae;
                         padding: 8px 10px; border-radius: 0 4px 4px 0; }}
.acc-meta  {{ display: flex; gap: 20px; font-size: 0.8rem; color: #5a6a8a; }}

/* ── Footer ── */
footer {{
  text-align: center;
  padding: 20px;
  font-size: 0.8rem;
  color: #8892b0;
  border-top: 1px solid #e8ecf4;
  background: white;
}}
footer a {{ color: #5a6a8a; text-decoration: none; }}
footer a:hover {{ text-decoration: underline; }}

/* ── Print ── */
@media print {{
  body {{ background: white; }}
  header {{ background: #1a1a2e !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .card {{ box-shadow: none; border: 1px solid #ddd; page-break-inside: avoid; }}
  details {{ page-break-inside: avoid; }}
  details[open] {{ page-break-inside: avoid; }}
}}
</style>
</head>
<body>

<header>
  <h1>📈 FinTradeBench Results</h1>
  <div class="subtitle">Model: <strong>{model}</strong> &nbsp;·&nbsp; {timestamp}</div>
  <div class="score-badge">{total_score:.1f} / 100</div>
</header>

<main>

  <!-- Meta -->
  <div class="card">
    <h2>Run Summary</h2>
    <div class="meta-grid">
      <div class="meta-item">
        <div class="label">Model</div>
        <div class="value" style="font-size:.85rem">{model}</div>
      </div>
      <div class="meta-item">
        <div class="label">Overall Score</div>
        <div class="value">{total_score:.1f} / 100</div>
      </div>
      <div class="meta-item">
        <div class="label">Timestamp</div>
        <div class="value" style="font-size:.85rem">{timestamp}</div>
      </div>
    </div>
  </div>

  <!-- Bar chart -->
  <div class="card">
    <h2>Category Scores</h2>
    {cat_bars_html}
  </div>

  <!-- Accordion -->
  <div class="card">
    <h2>Per-Question Results</h2>
    {rows_html}
  </div>

</main>

<footer>
  Powered by <strong>FinTradeBench</strong> &nbsp;·&nbsp;
  Built by <a href="https://heyneo.so" target="_blank">NEO</a>
</footer>

</body>
</html>"""

    path.write_text(html, encoding="utf-8")
    return str(path)


def print_leaderboard(
    reports: list[dict[str, Any]], console: Console | None = None
) -> None:
    """Print a leaderboard table sorted by total_score descending."""
    if console is None:
        console = Console()

    if not reports:
        console.print("[yellow]No reports found. Run a benchmark first.[/yellow]")
        return

    sorted_reports = sorted(reports, key=lambda r: r.get("total_score", 0.0), reverse=True)

    table = Table(title="FinTradeBench Leaderboard", box=box.ROUNDED)
    table.add_column("Rank", justify="right", style="dim", min_width=4)
    table.add_column("Model", style="cyan", min_width=30)
    table.add_column("Score", justify="right", style="bold green", min_width=8)
    table.add_column("Timestamp", min_width=18)

    for rank, r in enumerate(sorted_reports, 1):
        table.add_row(
            str(rank),
            r.get("model", "unknown"),
            f"{r.get('total_score', 0.0):.1f}",
            r.get("timestamp", ""),
        )

    console.print(table)
