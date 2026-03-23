#!/usr/bin/env python3
"""
FinTradeBench CLI — Financial Reasoning LLM Benchmarker

Usage:
    python benchmark.py --model <model_id>
    python benchmark.py --model <model_id> --dry-run
    python benchmark.py --model <model_id> --category market_analysis
    python benchmark.py --compare model1 model2 model3
    python benchmark.py --leaderboard
    python benchmark.py --list-models
    python benchmark.py --version
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

load_dotenv()

__version__ = "1.0.0"

console = Console()

MAX_QUESTIONS = int(os.environ.get("MAX_QUESTIONS", "0"))

VALID_CATEGORIES = [
    "market_analysis",
    "risk_assessment",
    "earnings_interpretation",
    "trading_strategy",
    "macro_economics",
]

RECOMMENDED_MODELS = [
    # (Display name, OpenRouter model ID, tier)
    # Premium — highest financial reasoning accuracy
    ("GPT-5.4 Pro",           "openai/gpt-5.4-pro",                     "Premium"),
    ("GPT-5.4",               "openai/gpt-5.4",                         "Premium"),
    ("Claude Opus 4.6",       "anthropic/claude-opus-4.6",              "Premium"),
    ("Claude Sonnet 4.6",     "anthropic/claude-sonnet-4.6",            "Premium"),
    ("Grok 4.20",             "x-ai/grok-4.20-beta",                    "Premium"),
    # Budget — great accuracy per dollar
    ("GPT-5.4 Mini",          "openai/gpt-5.4-mini",                    "Budget"),
    ("GPT-5.4 Nano",          "openai/gpt-5.4-nano",                    "Budget"),
    ("Mistral Small 4",       "mistralai/mistral-small-2603",           "Budget"),
    ("DeepSeek Chat",         "deepseek/deepseek-chat",                 "Budget"),
    ("DeepSeek R1",           "deepseek/deepseek-r1",                   "Budget"),
    ("Gemini 2.0 Flash",      "google/gemini-2.0-flash-001",            "Budget"),
    ("Qwen 2.5 72B",          "qwen/qwen-2.5-72b-instruct",             "Budget"),
    # Free tier — no credits needed
    ("Nemotron 3 Super 120B", "nvidia/nemotron-3-super-120b-a12b",      "Free"),
    ("Qwen 3.5 9B",           "qwen/qwen3.5-9b",                        "Free"),
    ("Llama 3.3 70B",         "meta-llama/llama-3.3-70b-instruct",      "Free"),
]


def print_banner() -> None:
    """Print the FinTradeBench startup banner."""
    content = (
        "[bold white]📈 FinTradeBench CLI[/bold white]  "
        f"[dim]v{__version__}[/dim]\n"
        "[white]Financial Reasoning LLM Evaluator[/white]\n"
        "[dim]65 questions · 5 categories[/dim]"
    )
    console.print(
        Panel(content, border_style="blue", expand=False, padding=(0, 2))
    )


def print_list_models() -> None:
    """Print a table of recommended models."""
    table = Table(title="Recommended Models", box=box.ROUNDED)
    table.add_column("Model",       style="cyan",   min_width=22)
    table.add_column("OpenRouter ID",               min_width=38)
    table.add_column("Tier",        justify="right", min_width=8)

    tier_colors = {"Premium": "bold green", "Budget": "yellow", "Free": "dim"}
    for name, model_id, tier in RECOMMENDED_MODELS:
        color = tier_colors.get(tier, "white")
        table.add_row(name, model_id, f"[{color}]{tier}[/{color}]")

    console.print(table)
    console.print(
        "\n[dim]Usage:[/dim]  python benchmark.py --model [cyan]<ID>[/cyan]\n"
    )


def _check_api_key(dry_run: bool) -> str:
    """Return API key or exit with a helpful error message."""
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    if not dry_run and not api_key:
        console.print()
        console.print("  [bold red]✗[/bold red] [red]OPENROUTER_API_KEY not set[/red]\n")
        console.print("  Set it with:   [bold]export OPENROUTER_API_KEY=sk-or-...[/bold]")
        console.print("  Or in .env:    [bold]echo \"OPENROUTER_API_KEY=sk-or-...\" > .env[/bold]\n")
        console.print("  Or use [bold]--dry-run[/bold] to test without an API key.\n")
        sys.exit(1)
    return api_key


def run_benchmark(model: str, dry_run: bool = False, category: str | None = None) -> None:
    from fintradebench.runner import BenchmarkRunner
    from fintradebench.reporter import build_report, save_report, print_results_table, save_html_report, REPORTS_DIR

    api_key = _check_api_key(dry_run)

    runner = BenchmarkRunner(model=model, api_key=api_key)
    results, total_score, category_scores = runner.run_full(
        dry_run=dry_run, category=category, max_questions=MAX_QUESTIONS
    )

    report = build_report(
        model=model,
        results=results,
        total_score=total_score,
        category_scores=category_scores,
    )

    saved_path = save_report(report, REPORTS_DIR)
    html_path = save_html_report(report, REPORTS_DIR)
    print_results_table(report, console=console)
    console.print(f"\n[dim]Report saved → {saved_path}[/dim]")
    console.print(f"[dim]HTML report  → {html_path}[/dim]")


def run_comparison(models: list[str], dry_run: bool = False) -> None:
    from fintradebench.runner import BenchmarkRunner
    from fintradebench.reporter import build_report, save_report, save_html_report, print_results_table, print_comparison_table, REPORTS_DIR

    api_key = _check_api_key(dry_run)

    reports = []
    for model in models:
        console.print(f"\n[bold]Benchmarking {model}...[/bold]")
        runner = BenchmarkRunner(model=model, api_key=api_key)
        results, total_score, category_scores = runner.run_full(
            dry_run=dry_run, max_questions=MAX_QUESTIONS
        )
        report = build_report(
            model=model,
            results=results,
            total_score=total_score,
            category_scores=category_scores,
        )
        save_report(report, REPORTS_DIR)
        save_html_report(report, REPORTS_DIR)
        print_results_table(report, console=console)
        reports.append(report)

    console.print("\n")
    print_comparison_table(reports, console=console)


def show_leaderboard() -> None:
    from fintradebench.reporter import load_all_reports, print_leaderboard, REPORTS_DIR

    reports = load_all_reports(REPORTS_DIR)
    print_leaderboard(reports, console=console)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="benchmark",
        description="FinTradeBench — Financial Reasoning LLM Benchmarker",
    )
    parser.add_argument(
        "--model",
        type=str,
        help="Model ID to benchmark (e.g. openai/gpt-4o)",
    )
    parser.add_argument(
        "--compare",
        nargs="+",
        metavar="MODEL",
        help="Benchmark multiple models and print a side-by-side comparison",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run with mocked responses (no API key required)",
    )
    parser.add_argument(
        "--leaderboard",
        action="store_true",
        help="Show leaderboard from saved reports",
    )
    parser.add_argument(
        "--category",
        type=str,
        help=(
            "Run only questions from this category. "
            f"Valid: {', '.join(VALID_CATEGORIES)}"
        ),
    )
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="Print a table of recommended OpenRouter models",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print version and exit",
    )

    args = parser.parse_args()

    if args.version:
        console.print(f"FinTradeBench CLI v{__version__}")
        return

    if args.list_models:
        print_banner()
        print_list_models()
        return

    if args.category and args.category not in VALID_CATEGORIES:
        console.print(
            f"[red]Error:[/red] Invalid category '{args.category}'. "
            f"Valid options: {', '.join(VALID_CATEGORIES)}"
        )
        sys.exit(1)

    if args.leaderboard:
        show_leaderboard()
    elif args.compare:
        print_banner()
        run_comparison(args.compare, dry_run=args.dry_run)
    elif args.model:
        print_banner()
        run_benchmark(args.model, dry_run=args.dry_run, category=args.category)
    elif os.getenv("DEFAULT_MODEL"):
        # Allow `DEFAULT_MODEL=openai/gpt-4o python benchmark.py` without --model flag
        print_banner()
        run_benchmark(os.getenv("DEFAULT_MODEL"), dry_run=args.dry_run, category=args.category)
    else:
        print_banner()
        console.print(
            "\n  [yellow]Tip:[/yellow] set a model with [cyan]--model <id>[/cyan] "
            "or [cyan]DEFAULT_MODEL=<id>[/cyan] in .env\n"
            "  Run [cyan]python benchmark.py --list-models[/cyan] to see options.\n"
        )
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
