<div align="center">

![NeuroShell](https://img.shields.io/badge/NeuroShell-v0.1.0-8A2BE2?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/LLM-Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen?style=for-the-badge)

<pre>
███╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ███████╗██╗  ██╗███████╗██╗     ██╗
████╗  ██║██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔════╝██║  ██║██╔════╝██║     ██║
██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║   ██║███████╗███████║█████╗  ██║     ██║
██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║   ██║╚════██║██╔══██║██╔══╝  ██║     ██║
██║ ╚████║███████╗╚██████╔╝██║  ██║╚██████╔╝███████║██║  ██║███████╗███████╗███████╗
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
</pre>

### 🧠 An open-source, Linux-first personal AI companion.

**The foundation of NeuroLink OS.**

[Getting Started](#-getting-started) · [Features](#-features) · [Usage](#-usage) · [Roadmap](#-master-roadmap) · [Architecture](#-architecture)

</div>

---

NeuroShell isn't a chatbot wrapper or a "Jarvis clone." It's being built deliberately across 16 stages to evolve from a basic text interface into a fully autonomous Linux computer agent.

**Currently at:** **Stage 2** (Tools & Function Execution)

```text
You:        "Hello NeuroShell."
NeuroShell: "Hey! What's up?"

You:        "My name is Keerthi."
NeuroShell: "Nice to meet you, Keerthi!"

You:        "What is my name?"
NeuroShell: "Your name is Keerthi."
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- A Google Gemini API Key ([Get one free here](https://aistudio.google.com/apikey))

### Step 1: Clone the Repository
```bash
git clone https://github.com/keerthi-180205/neuroshell.git
cd neuroshell
```

### Step 2: Set Up the Environment
Create a virtual environment so NeuroShell doesn't conflict with your global Python packages:
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure API Keys
Copy the example environment file and add your actual API key:
```bash
cp .env.example .env
```
Open `.env` in your text editor and replace `your_api_key_here` with your real Gemini API key.

### Step 5: Run NeuroShell
```bash
python run.py
```

---

## 🏗️ Architecture

NeuroShell is built with strict modularity. The CLI never talks directly to the LLM.

```text
                    USER
                      │
                      ↓
                  CLI INPUT
                      │
                      ↓
               ┌─────────────┐
               │ ORCHESTRATOR│
               └──────┬──────┘
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
      CONTEXT       LLM        TOOLS
      MANAGER      LAYER      INTERFACE
          │           │           │
          │        Gemini       Scaffold
          │           │           │
          └───────────┼───────────┘
                      ↓
                   RESPONSE
                      │
                      ↓
                  CLI OUTPUT
                      │
                      ↓
                     USER
```

### Project Structure
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

---

## 🗺️ Master Roadmap

The project is structured across 3 major versions and 16 distinct stages. You can track our real-time progress in the [`progress.md`](progress.md) file.

### V1 — PERSONAL AI COMPANION
- ✅ **Stage 1:** Basic Text Interaction Core
- 🚧 **Stage 2:** Tools & Function Execution *(Current)*
- 🎯 **Stage 3:** Voice Interaction
- 🎯 **Stage 4:** Personality & Personalization
- 🎯 **Stage 5:** Long-Term Memory
- 🎯 **Stage 6:** Knowledge / RAG

### V2 — AI COMPUTER AGENT
- 🎯 **Stage 7:** Linux System Control
- 🎯 **Stage 8:** File & Application Control
- 🎯 **Stage 9:** Browser & Web Automation
- 🎯 **Stage 10:** Developer / DevOps Tools
- 🎯 **Stage 11:** Security & Permission System

### V3 — AUTONOMOUS PERSONAL COMPANION
- 🎯 **Stage 12:** Planning & Multi-Step Tasks
- 🎯 **Stage 13:** Observation & Error Recovery
- 🎯 **Stage 14:** Proactive Assistance
- 🎯 **Stage 15:** Personal Workflow Intelligence
- 🎯 **Stage 16:** Plugin Ecosystem & V3 Release

---

## 🔒 Security & Privacy

- **API Keys are safe:** The `.env` file is explicitly ignored by Git. Your Gemini API key will never be committed to the repository.
- **Strict Boundaries:** The orchestrator architecture ensures the LLM has zero access to your file system or terminal shell (until sandboxed permission systems are introduced in V2).

---

## 📄 License
Licensed under the [Apache License 2.0](LICENSE).
