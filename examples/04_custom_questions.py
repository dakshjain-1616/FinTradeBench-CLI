"""
Example 4: Add custom questions to the benchmark dataset.

Usage:
    python examples/04_custom_questions.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fintradebench import QUESTIONS, BenchmarkRunner, build_report, print_results_table
from rich.console import Console

console = Console()

CUSTOM_QUESTIONS = [
    {
        "id": "CUSTOM001",
        "category": "custom",
        "question": "A company has a debt-to-equity ratio of 2.5. Is this concerning?",
        "reference_answer": "A D/E ratio of 2.5 is high and suggests the company uses significantly more debt than equity, increasing financial risk, especially in rising interest rate environments.",
        "keywords": ["debt", "equity", "ratio", "risk", "interest"],
    },
    {
        "id": "CUSTOM002",
        "category": "custom",
        "question": "What does a negative free cash flow for 3 consecutive quarters indicate?",
        "reference_answer": "Persistent negative free cash flow suggests the company spends more than it earns from operations, which may indicate heavy investment, poor profitability, or unsustainable business model.",
        "keywords": ["free cash flow", "negative", "operations", "investment", "profitability"],
    },
]

def main():
    # Extend the dataset with custom questions
    extended = QUESTIONS + CUSTOM_QUESTIONS
    console.print(f"Dataset extended: {len(QUESTIONS)} → {len(extended)} questions")

    # Score a mock answer against a custom question
    from fintradebench import score_answer
    answer = "A high debt-to-equity ratio signals elevated financial risk and heavy reliance on debt."
    score = score_answer(answer, CUSTOM_QUESTIONS[0])
    console.print(f"\nCustom question score: [bold green]{score:.2f}[/bold green]")
    console.print("[dim]Tip: add CUSTOM_QUESTIONS to fintradebench/dataset.py to persist them.[/dim]")

if __name__ == "__main__":
    main()
