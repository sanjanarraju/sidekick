---
title: Sidekick Personal Co-Worker
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
suggested_hardware: cpu-basic
---

# 🤖 Sidekick Personal Co-Worker

An autonomous AI agent loop powered by **LangGraph**, **Gradio**, and **LangChain**. Sidekick acts as a personal co-worker that utilizes multi-agent evaluation patterns to continuously iterate on a task until it completely satisfies your predefined success criteria.

## 🛠️ Features & Tools
- **Web Search & Browsing**: Powered by Playwright and Google Serper API.
- **Self-Evaluating Feedback Loop**: Includes a worker LLM built to handle tasks and an automated Evaluator LLM ensuring output benchmarks are met before responding.
- **System Interactions**: Equipped with local file management sandboxing and instant push notifications via Pushover.

## ⚙️ Space Setup & Environment Variables

For this Space to run properly, you must configure the following **Secrets** in your Hugging Face Space settings (**Settings > Variables and Secrets**):

| Secret Name | Description |
| :--- | :--- |
| `OPENAI_API_KEY` | Required for the `gpt-4o-mini` worker and evaluator LLMs. |
| `SERPER_API_KEY` | Required for Google search results (`GoogleSerperAPIWrapper`). |
| `PUSHOVER_TOKEN` | (Optional) Your Pushover application token for notifications. |
| `PUSHOVER_USER` | (Optional) Your Pushover user key. |

---

## 🏗️ Core Directory Structure

To deploy successfully, ensure your Space repository contains only these clean core files:
```text
.
├── app.py              # Gradio web interface layout and event listeners
├── sidekick.py         # LangGraph state machine, worker, and evaluator nodes
├── sidekick_tools.py   # Tool suites (Playwright, File management, Search, Wiki)
├── requirements.txt    # Python package dependencies
└── README.md           # HF Space metadata and documentation