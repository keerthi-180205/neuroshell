# NeuroShell

An open-source, Linux-first personal AI companion.

![NeuroShell](https://img.shields.io/badge/NeuroShell-v0.1.0-8A2BE2)
![License](https://img.shields.io/badge/License-Apache%202.0-blue)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![LLM](https://img.shields.io/badge/LLM-Google%20Gemini-4285F4)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

NeuroShell is not a chatbot wrapper or a "Jarvis clone." It is being built deliberately across 16 stages, evolving from a basic text interface into a fully autonomous Linux computer agent.

**Current status:** Stage 2 — Tools & Function Execution

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Security & Privacy](#security--privacy)
- [Contributing](#contributing)
- [License](#license)

## Overview

```text
You:        "Hello NeuroShell."
NeuroShell: "Hey! What's up?"

You:        "My name is Keerthi."
NeuroShell: "Nice to meet you, Keerthi!"

You:        "What is my name?"
NeuroShell: "Your name is Keerthi."
```

## Getting Started

### Prerequisites

- Python 3.11+
- A Google Gemini API key ([get one here](https://aistudio.google.com/apikey))

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/keerthi-180205/neuroshell.git
   cd neuroshell
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your API key:

   ```bash
   cp .env.example .env
   ```

   Open `.env` and replace `your_api_key_here` with your actual Gemini API key.

5. Run NeuroShell:

   ```bash
   python run.py
   ```

## Usage

Run `python run.py` to start an interactive session. Type a message and press Enter; type `exit` to quit.

## Architecture

NeuroShell is built with strict modularity. The CLI never talks directly to the LLM — all requests pass through an orchestrator that coordinates context, the LLM layer, and available tools.

```text
                    USER
                      │
                      ▼
                  CLI INPUT
                      │
                      ▼
               ┌─────────────┐
               │ ORCHESTRATOR│
               └──────┬──────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      CONTEXT       LLM        TOOLS
      MANAGER      LAYER      INTERFACE
          │           │           │
          │        Gemini       Scaffold
          │           │           │
          └───────────┼───────────┘
                      ▼
                   RESPONSE
                      │
                      ▼
                  CLI OUTPUT
                      │
                      ▼
                     USER
```

## Project Structure

```text
neuroshell/
│
├── app/
│   ├── core/
│   │   ├── config.py          # Secure environment loading
│   │   ├── context.py         # Short-term conversation memory
│   │   ├── llm.py             # Gemini provider abstraction
│   │   └── orchestrator.py    # Central coordination logic
│   │
│   ├── interfaces/
│   │   └── text.py            # Rich terminal UI
│   │
│   ├── prompts/
│   │   └── system_prompt.py   # AI personality boundaries
│   │
│   └── tools/
│       └── base.py            # Tool architecture (Stage 2)
│
├── tests/                     # Unit tests (pytest)
├── .env.example               # Config template
├── requirements.txt           # Dependencies
├── progress.md                # Detailed project tracker
└── run.py                     # Entry point
```

## Roadmap

The project is structured across three major versions and 16 stages. Real-time progress is tracked in [`progress.md`](progress.md).

**V1 — Personal AI Companion**

| Stage | Description | Status |
|---|---|---|
| 1 | Basic Text Interaction Core | Done |
| 2 | Tools & Function Execution | In progress |
| 3 | Voice Interaction | Planned |
| 4 | Personality & Personalization | Planned |
| 5 | Long-Term Memory | Planned |
| 6 | Knowledge / RAG | Planned |

**V2 — AI Computer Agent**

| Stage | Description | Status |
|---|---|---|
| 7 | Linux System Control | Planned |
| 8 | File & Application Control | Planned |
| 9 | Browser & Web Automation | Planned |
| 10 | Developer / DevOps Tools | Planned |
| 11 | Security & Permission System | Planned |

**V3 — Autonomous Personal Companion**

| Stage | Description | Status |
|---|---|---|
| 12 | Planning & Multi-Step Tasks | Planned |
| 13 | Observation & Error Recovery | Planned |
| 14 | Proactive Assistance | Planned |
| 15 | Personal Workflow Intelligence | Planned |
| 16 | Plugin Ecosystem & V3 Release | Planned |

## Security & Privacy

- **API keys are safe.** The `.env` file is explicitly ignored by Git; your Gemini API key is never committed to the repository.
- **Strict boundaries.** The orchestrator architecture ensures the LLM has zero access to the file system or terminal shell until sandboxed permission systems are introduced in V2.

## Contributing

Contributions are welcome. Please open an issue to discuss significant changes before submitting a pull request. Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat`, `fix`, `docs`, `refactor`, `test`, `chore`).

## License

Licensed under the [Apache License 2.0](LICENSE).