"""
Example 1: Run a quick dry-run benchmark and print results.

Usage:
    python examples/01_quick_benchmark.py

No API key needed - uses dry-run mode.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fintradebench import BenchmarkRunner, build_report, print_results_table
from rich.console import Console

console = Console()

def main():
    model = os.getenv("BENCHMARK_MODEL", "openai/gpt-4o")
    runner = BenchmarkRunner(model=model, api_key=os.getenv("OPENROUTER_API_KEY", ""))
    results, total_score, category_scores = runner.run_full(dry_run=True)

    report = build_report(
        model=f"{model} (dry-run)",
        results=results,
        total_score=total_score,
        category_scores=category_scores,
    )
    print_results_table(report, console=console)
    console.print(f"\n[bold green]Overall Score: {total_score:.1f}/100[/bold green]")

if __name__ == "__main__":
    main()
