# Sidekick

A browser-operating agent designed for open-ended tasks. Ask Sidekick to find the best restaurants in NYC, and it will spin up a live browser instance using Playwright, navigate the web, research options in real time, and compile the results.

Powered by **LangGraph**, **Gradio**, and **LangChain**, Sidekick operates as an autonomous, self-correcting co-worker. It doesn't just run a search—it continuously evaluates its own output against your predefined success criteria, refining its approach until the task is fully completed.

---

## How the Agent Loop Works

When you submit a request, Sidekick executes an autonomous execution and evaluation cycle:

1. **User Input**: You provide a task/request alongside your explicit **Success Criteria**.
2. **Worker Node**: The primary LLM (`gpt-4o-mini`) evaluates the prompt and sequentially calls its tools (real-time Playwright web browsing, Google search, Wikipedia) to gather information.
3. **Evaluator Node**: A secondary structured LLM reviews the worker's output against your original Success Criteria.
4. **Self-Correction Loop**: If the criteria are not fully met, the evaluator generates explicit feedback and sends the worker back to the web browser to fix the gaps. If met, the loop terminates and outputs the final result.

---

## Core Project Files

This repository is optimized down to only the core standalone deployment files:
* **`app.py`**: The web interface layer built with Gradio. Handles the UI blocks, chat states, and real-time event listeners.
* **`sidekick.py`**: The core state machine logic. Defines the LangGraph agent graph, worker, and evaluation router.
* **`sidekick_tools.py`**: The tool integration layer giving the agent access to live Chromium browsing via Playwright, Serper API search, Wikipedia, and local file management.
* **`requirements.txt`**: Complete list of Python package dependencies.

---

## How to Run It

Open your terminal inside this project folder and execute the following commands in order to get the application up and running:

### Set Environment Variables And Run
Set your API keys so the agent has the credentials to think and execute web searches:

```bash
export OPENAI_API_KEY="your-actual-openai-key"
export SERPER_API_KEY="your-actual-serper-key"

uv run playwright install
uv run app.py
```

<img width="1534" height="626" alt="Screenshot 2026-06-25 at 6 21 55 PM" src="https://github.com/user-attachments/assets/72a67a26-1806-4c13-98fb-568b71e236fa" />

<img width="1511" height="586" alt="Screenshot 2026-06-25 at 6 24 50 PM" src="https://github.com/user-attachments/assets/640fd268-6625-4dde-90ee-08b1d986a09b" />




