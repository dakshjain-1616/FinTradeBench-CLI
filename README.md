[![Try NEO in VS Code](https://img.shields.io/badge/VS%20Code-Try%20NEO-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://marketplace.visualstudio.com/items?itemName=NeoResearchInc.heyneo)
[![Built autonomously using NEO](https://img.shields.io/badge/Built%20with-NEO%20Autonomous%20AI-blueviolet?style=flat-square)](https://heyneo.so)
[![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat-square)](https://python.org)
[![Tests](https://img.shields.io/badge/tests-34%20passing-brightgreen?style=flat-square)](#running-tests)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

# 📈 FinTradeBench CLI

> Built autonomously using [NEO](https://heyneo.so) — your autonomous AI Agent

**Benchmark any LLM on financial reasoning. One command. Beautiful results.**

---

## What is this?

FinTradeBench is a CLI tool that evaluates any LLM's financial reasoning ability using 65 curated questions across 5 categories — all embedded directly in the source, no external downloads required. Point it at any model available on OpenRouter, run one command, and get back scored JSON and HTML reports plus a persistent leaderboard.

## ✨ Features

- **65 embedded questions** across 5 categories — no downloads, no setup
- **Works with 200+ models** via [OpenRouter](https://openrouter.ai) (GPT-4, Claude, Gemini, Llama, DeepSeek, and more)
- **Keyword overlap + exact match scoring** — 0–1 per question, 0–100 overall
- **Confidence scoring** — model self-rates each answer 1–5
- **Timed answers** — wall-clock seconds recorded per question
- **Rich terminal UI** — startup banner, progress bar, category breakdown table, per-question results
- **JSON + HTML reports** — auto-saved after every run; HTML has animated bar charts and an expandable accordion per question
- **Persistent leaderboard** — compare all past runs sorted by score
- **`--compare`** — benchmark multiple models side-by-side in one command
- **`--category`** — filter to a single question category
- **`--dry-run`** — full pipeline test without spending API credits
- **`--list-models`** — browse recommended models with tier info

## 🚀 Quick Start

```bash
git clone https://github.com/dakshjain-1616/FinTradeBench-CLI
cd fintradebench-cli
pip install -r requirements.txt
cp .env.example .env       # add OPENROUTER_API_KEY
python benchmark.py --model openai/gpt-4o
```

**No API key?** Try the demo:
```bash
python demo.py
```

## 📊 Usage

```bash
# Run full benchmark
python benchmark.py --model openai/gpt-4o

# Dry run (no API key needed)
python benchmark.py --model openai/gpt-4o --dry-run

# Benchmark only one category
python benchmark.py --model openai/gpt-4o --category market_analysis

# Compare two models side-by-side
python benchmark.py --compare openai/gpt-4o deepseek/deepseek-chat

# Show leaderboard of all past runs
python benchmark.py --leaderboard

# List recommended models
python benchmark.py --list-models
```

## 🤖 Supported Models

FinTradeBench works with **any model on [OpenRouter](https://openrouter.ai/models)** — 200+. Run `python benchmark.py --list-models` for a quick reference.

| Model | OpenRouter ID | Tier | Notes |
|-------|--------------|------|-------|
| GPT-5.4 Pro | `openai/gpt-5.4-pro` | 💛 Premium | OpenAI flagship, 1M ctx |
| GPT-5.4 | `openai/gpt-5.4` | 💛 Premium | 1M context window |
| Claude Opus 4.6 | `anthropic/claude-opus-4.6` | 💛 Premium | Anthropic flagship, 1M ctx |
| Claude Sonnet 4.6 | `anthropic/claude-sonnet-4.6` | 💛 Premium | Fast + smart, 1M ctx |
| Grok 4.20 | `x-ai/grok-4.20-beta` | 💛 Premium | xAI, 2M context window |
| **DeepSeek Chat** | `deepseek/deepseek-chat` | 💚 Budget | **Recommended default** — great value |
| GPT-5.4 Mini | `openai/gpt-5.4-mini` | 💚 Budget | Fast GPT-5 class, 400k ctx |
| GPT-5.4 Nano | `openai/gpt-5.4-nano` | 💚 Budget | Ultra-fast, 400k ctx |
| Mistral Small 4 | `mistralai/mistral-small-2603` | 💚 Budget | Mistral latest, 262k ctx |
| DeepSeek R1 | `deepseek/deepseek-r1` | 💚 Budget | Strong reasoning |
| Gemini 2.0 Flash | `google/gemini-2.0-flash-001` | 💚 Budget | Speed + quality balance |
| Qwen 2.5 72B | `qwen/qwen-2.5-72b-instruct` | 💚 Budget | Multilingual |
| Nemotron 3 Super 120B | `nvidia/nemotron-3-super-120b-a12b` | 🆓 Free | NVIDIA 120B, 262k ctx |
| Qwen 3.5 9B | `qwen/qwen3.5-9b` | 🆓 Free | Qwen latest, 256k ctx |
| Llama 3.3 70B | `meta-llama/llama-3.3-70b-instruct` | 🆓 Free | Best open-source option |

### Switching models

```bash
# Via CLI flag
python benchmark.py --model anthropic/claude-3.5-sonnet

# Via env var (skip --model on every run)
DEFAULT_MODEL=openai/gpt-4o python benchmark.py

# Or set in .env and just run:
python benchmark.py
```

---

## 📂 Question Categories

| Category                | Key                       | Questions |
|-------------------------|---------------------------|-----------|
| Market Analysis         | `market_analysis`         | 13        |
| Risk Assessment         | `risk_assessment`         | 14        |
| Earnings Interpretation | `earnings_interpretation` | 14        |
| Trading Strategy        | `trading_strategy`        | 13        |
| Macro Economics         | `macro_economics`         | 14        |
| **Total**               |                           | **68**    |

## 📋 Scoring

| Method          | Description                                                        |
|-----------------|--------------------------------------------------------------------|
| Exact match     | 1.0 if the answer matches the reference exactly (case-insensitive) |
| Keyword overlap | Fraction of expected keywords found in the model's answer          |
| Overall score   | Average of all per-question scores × 100 (0–100 scale)            |
| Confidence      | Model rates its own answer 1 (guessing) → 5 (certain)             |
| Time            | Wall-clock seconds for the model to produce each answer            |

## 📄 Reports

After each run both a JSON and HTML report are saved to `reports/`:

```
reports/<model_id>_<timestamp>.json
reports/<model_id>_<timestamp>.html
```

**JSON schema:**
```json
{
  "model": "openai/gpt-4o",
  "timestamp": "20240101T120000Z",
  "total_score": 74.3,
  "avg_confidence": 4.1,
  "avg_time_s": 1.83,
  "category_scores": {
    "market_analysis": 0.82,
    "risk_assessment": 0.71
  },
  "results": [
    {
      "id": "MA001",
      "category": "market_analysis",
      "score": 0.8,
      "confidence": 4.0,
      "time_taken_s": 1.2,
      "keywords_matched": "4/5",
      "answer": "...",
      "reference_answer": "..."
    }
  ]
}
```

**HTML report** — a self-contained single-file page with:
- Animated bar chart (bars fill in on page load)
- Expandable accordion per question showing full question, model answer, and reference
- Print-friendly layout

## 🌍 Environment Variables

Copy `.env.example` to `.env`. All values except `OPENROUTER_API_KEY` are optional.

| Variable              | Default                          | Description                                  |
|-----------------------|----------------------------------|----------------------------------------------|
| `OPENROUTER_API_KEY`  | *(required for real runs)*       | Your OpenRouter API key — [get one here](https://openrouter.ai) |
| `DEFAULT_MODEL`       | *(none)*                         | Model ID to use when `--model` flag is not provided |
| `OPENROUTER_BASE_URL` | `https://openrouter.ai/api/v1`   | Override the OpenRouter API endpoint         |
| `REPORTS_DIR`         | `reports`                        | Directory where JSON/HTML reports are saved  |
| `MAX_QUESTIONS`       | `0` (no limit)                   | Cap the number of questions (useful for quick tests) |

## 🧪 Running Tests

```bash
pytest tests/ -v   # 34 tests, all passing
```

## 💡 Examples

```bash
# Quick dry-run benchmark (no API key needed)
python examples/01_quick_benchmark.py

# Compare two models side-by-side
python examples/02_compare_models.py

# Inspect all questions in a category
python examples/03_category_deep_dive.py market_analysis

# Add custom questions to the dataset
python examples/04_custom_questions.py
```

### Example output - `benchmark.py --model deepseek/deepseek-chat`

```
╔══════════════════════════════════════════╗
║  📈 FinTradeBench CLI  v1.0.0           ║
║  Financial Reasoning LLM Evaluator      ║
╚══════════════════════════════════════════╝

Running FinTradeBench on deepseek/deepseek-chat  ████████████████ 65/65

FinTradeBench Results - deepseek/deepseek-chat
Overall Score: 61.4 / 100

╭───────────────────────────┬───────────┬────────╮
│ Category                  │ Avg Score │    Pct │
├───────────────────────────┼───────────┼────────┤
│ Market Analysis           │     0.721 │  72.1% │
│ Risk Assessment           │     0.634 │  63.4% │
│ Earnings Interpretation   │     0.598 │  59.8% │
│ Trading Strategy          │     0.612 │  61.2% │
│ Macro Economics           │     0.583 │  58.3% │
╰───────────────────────────┴───────────┴────────╯

Report saved → reports/deepseek_deepseek-chat_20260321T120000Z.json
```

## 📁 Project Structure

```
fintradebench-cli/
├── fintradebench/            # Package
│   ├── __init__.py           # Exports BenchmarkRunner, score_answer, build_report, QUESTIONS
│   ├── dataset.py            # 68 embedded financial questions
│   ├── runner.py             # BenchmarkRunner — LLM calls, progress bar, scoring
│   ├── scorer.py             # Keyword overlap + exact match scoring functions
│   └── reporter.py           # JSON + HTML report generation, leaderboard, tables
├── examples/
│   ├── README.md
│   ├── 01_quick_benchmark.py
│   ├── 02_compare_models.py
│   ├── 03_category_deep_dive.py
│   └── 04_custom_questions.py
├── benchmark.py              # CLI entry point — flags, banner, orchestration
├── demo.py                   # 5-question dry-run demo (no API key)
├── requirements.txt
├── .env.example
└── tests/
    ├── test_dataset.py
    ├── test_scorer.py
    ├── test_runner.py
    ├── test_reporter.py
    └── test_enhancements.py
```

## 📄 License

MIT

---

_Built autonomously using [NEO](https://heyneo.so) — your autonomous AI Agent_
