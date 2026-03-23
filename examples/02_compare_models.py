"""
Example 2: Compare two models side by side (dry-run).

Usage:
    python examples/02_compare_models.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fintradebench import BenchmarkRunner, build_report
from fintradebench.reporter import print_comparison_table
from rich.console import Console

console = Console()

MODELS = ["openai/gpt-4o", "anthropic/claude-3.5-sonnet"]

def main():
    reports = []
    for model in MODELS:
        runner = BenchmarkRunner(model=model, api_key="")
        results, total, cat_scores = runner.run_full(dry_run=True)
        reports.append(build_report(model=model, results=results,
                                    total_score=total, category_scores=cat_scores))
        console.print(f"[dim]Benchmarked {model}: {total:.1f}/100[/dim]")

    console.print("\n[bold]Side-by-Side Comparison[/bold]")
    print_comparison_table(reports, console=console)

if __name__ == "__main__":
    main()
