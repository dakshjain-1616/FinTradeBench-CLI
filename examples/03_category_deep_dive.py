"""
Example 3: Deep dive into the Market Analysis category.

Usage:
    python examples/03_category_deep_dive.py [category]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fintradebench import QUESTIONS, score_answer
from rich.console import Console
from rich.table import Table

console = Console()

def main():
    category = sys.argv[1] if len(sys.argv) > 1 else "market_analysis"
    questions = [q for q in QUESTIONS if q["category"] == category]

    if not questions:
        console.print(f"[red]Unknown category: {category}[/red]")
        console.print(f"Available: {sorted(set(q['category'] for q in QUESTIONS))}")
        sys.exit(1)

    console.print(f"\n[bold blue]Category: {category}[/bold blue] ({len(questions)} questions)\n")

    table = Table(show_header=True, header_style="bold")
    table.add_column("ID", style="dim", width=8)
    table.add_column("Question", width=50)
    table.add_column("Keywords", width=30)

    for q in questions:
        table.add_row(
            q["id"],
            q["question"][:80] + ("…" if len(q["question"]) > 80 else ""),
            ", ".join(q.get("keywords", [])[:4]),
        )

    console.print(table)
    console.print(f"\n[dim]Run: python benchmark.py --model openai/gpt-4o --category {category}[/dim]")

if __name__ == "__main__":
    main()
