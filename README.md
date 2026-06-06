<div align="center">

<img src="https://img.shields.io/badge/NeuroShell-v0.1.0-6C63FF?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />

<br/><br/>

```
███╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ███████╗██╗  ██╗███████╗██╗     ██╗
████╗  ██║██╔════╝██║   ██║██╔══██╗██╔═══██╗██╔════╝██║  ██║██╔════╝██║     ██║
██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║   ██║███████╗███████║█████╗  ██║     ██║
██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║   ██║╚════██║██╔══██║██╔══╝  ██║     ██║
██║ ╚████║███████╗╚██████╔╝██║  ██║╚██████╔╝███████║██║  ██║███████╗███████╗███████╗
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
```

### 🧠 The AI-powered CLI that understands you. *(In Development)*
### The foundation of **NeuroLink OS**.

<br/>

**[Getting Started](#-installation) · [Features](#-features) · [Usage](#-usage) · [Roadmap](#-roadmap) · [Contributing](#-contributing)**

<br/>

</div>

---

## 🌟 What is NeuroShell?

**NeuroShell** is the command-line foundation of **NeuroLink OS** — an open-source, local-first AI intelligence layer being built for your machine. The vision: instead of memorizing commands, you express intent in plain English and a local LLM figures out the rest.

This is **v0.1 — the very first commit**. The CLI loop is live. The AI engine is being built.

Here's what it will do when complete:

```bash
> explain how recursion works in Python
> summarize the contents of my notes.txt
> what is a docker container?
```

> ⚠️ **Current state:** NeuroShell v0.1 is the working CLI skeleton. Ollama integration, intent detection, and AI responses are actively in development. Follow the repo to get notified when they land.

> 💡 **NeuroShell is v0.1 of NeuroLink OS** — an ambitious open-source project to build a full AI intelligence layer for your machine. This is where it starts.

---

## ✨ Features

### v0.1 — Available Now

| Feature | Status | Description |
|---|---|---|
| ⚡ **CLI Loop** | ✅ Live | Interactive terminal loop — runs, accepts input, exits cleanly |
| 🗣️ **Natural Language Input** | 🔨 In Development | Plain English → LLM routing |
| 🧩 **Intent Detection** | 🔨 In Development | Detects `explain`, `summarize`, or general queries |
| 🤖 **Local LLM via Ollama** | 🔨 In Development | Runs on `llama3` or any Ollama-supported model |
| 🎨 **Rich Terminal Output** | 🔨 In Development | Formatted responses powered by `rich` |
| 🔒 **100% Local & Private** | 🎯 Planned | Zero data leaves your machine. No API keys needed. |

---

## 🏗️ Project Structure

```
neuroshell/                    ← repo root
│
├── neuroshell.py              # ✅ LIVE — CLI loop (8 lines, input → echo → exit)
├── LICENSE                    # ✅ Apache 2.0
├── README.md                  # ✅ This file
├── .gitignore                 # ✅ Python + venv rules
│
├── core/                      # 🎯 PLANNED — v0.1 intent detection
│   ├── command_parser.py      # 🎯 Rule-based intent detection
│   └── context_manager.py     # 🎯 Placeholder — v0.2 memory system
│
├── llm/                       # 🎯 PLANNED — v0.1 Ollama integration
│   └── ollama_client.py       # 🎯 Ollama API client
│
├── utils/                     # 🎯 PLANNED — v0.1 output formatting
│   └── formatter.py           # 🎯 Rich terminal output
│
└── plugins/                   # 🎯 PLANNED — v0.3 plugin ecosystem
```

> 📌 **Current reality:** Only `neuroshell.py` exists. All other modules are actively being built.

---

## 📦 Installation

### Prerequisites

Before you begin, ensure you have:

- **Python 3.11+** installed → [Download](https://www.python.org/downloads/)
- **Ollama** *(optional for now — required in future versions)* → [Download](https://ollama.ai)

> ⚠️ Ollama integration is in development. You can run the current CLI without it.

### Step 1: Clone the Repository

```bash
git clone https://github.com/keerthi-180205/neuroshell.git
cd neuroshell
```

### Step 2: Run NeuroShell

```bash
python neuroshell.py
```

> No dependencies needed yet. `requirements.txt` will be added once LLM integration begins.

> 🔨 **Ollama integration is in development.** Steps to connect to a local LLM will be added in the next update.

---

## 🚀 Usage

Once running, you'll see the NeuroShell prompt. Type anything and press Enter:

```
> python neuroshell.py

> hello neuroshell
[NeuroShell]: You said -> hello neuroshell

> explain recursion
[NeuroShell]: You said -> explain recursion

> exit
Exiting NeuroShell...
```

> ⚠️ **AI responses are in development.** The current version echoes your input back. Once Ollama integration is complete, queries will be routed to a local LLM for intelligent responses.

### Intent Keywords *(In Development)*

| You say... | NeuroShell will do... | Status |
|---|---|---|
| `explain <topic>` | Explains the concept in detail | 🎯 Planned |
| `summarize <topic>` | Returns a concise summary | 🎯 Planned |
| anything else | General intelligent query | 🎯 Planned |

---

## ⚙️ Configuration

> 🔨 **Configuration is in development.** Once Ollama integration is complete, NeuroShell will connect to a local LLM with the following defaults:

```
Ollama URL : http://localhost:11434   ← coming in next update
Model      : llama3                   ← configurable via ollama_client.py
```

You'll be able to change the model in `llm/ollama_client.py`:

```python
MODEL = "llama3"          # change to "mistral", "phi3", "gemma", etc.
```

> Browse all supported models at [ollama.ai/library](https://ollama.ai/library)

---

## 🗺️ Roadmap

NeuroShell is **v0.1** of a much larger vision. Here's where we're headed:

### 🔨 v0.1 — NeuroShell *(In Progress)*
- [x] Working CLI loop (input → echo → exit)
- [ ] Intent detection (explain / summarize / general)
- [ ] Ollama local LLM integration
- [ ] Rich terminal output
- [ ] Modular folder structure (core/, llm/, utils/)

### 🔜 v0.2 — NeuroBrain *(Month 9)*
- [ ] Persistent conversation memory via ChromaDB
- [ ] Multi-turn interaction (context-aware)
- [ ] Knowledge graph of your machine (NetworkX)
- [ ] `neuro remember` / `neuro forget` commands
- [ ] Passive awareness mode — proactive suggestions

### 🔮 v0.3 — NeuroSwarm *(Month 10)*
- [ ] Multi-agent parallel execution (LangGraph)
- [ ] Plugin API — community-built NeuroPlugins
- [ ] Time-travel undo — `neuro undo last 3 actions`
- [ ] Textual TUI dashboard (NeuroInsights)
- [ ] Plugin marketplace launch

### 🌐 v1.0 — NeuroLink OS *(Month 11–12)*
- [ ] Voice input via OpenAI Whisper (local)
- [ ] Vision input — screenshot a bug, say "fix this"
- [ ] Cross-platform: Linux, macOS, Windows (beta)
- [ ] Optional cloud sync of memory graph
- [ ] Full MkDocs documentation + contributor guide

---

## 🛠️ Tech Stack

| Layer | Technology | Status |
|---|---|---|
| Language | Python 3.11+ | ✅ Active |
| LLM Runtime | Ollama (local, GGUF models) | 🔨 In Development |
| Terminal UI | Rich | 🔨 In Development |
| HTTP Client | Requests | 🔨 In Development |
| Memory | ChromaDB + NetworkX + SQLite | 🎯 Planned v0.2 |
| Agents | LangGraph + AsyncIO | 🎯 Planned v0.3 |
| Voice | OpenAI Whisper (local) | 🎯 Planned v1.0 |
| Plugins | PyPI entry_points | 🎯 Planned v0.3 |

---

## 🤝 Contributing

NeuroShell is open to contributions of all kinds — from bug fixes to entirely new agent ideas.

### Quick Start for Contributors

```bash
# 1. Fork the repo on GitHub

# 2. Clone your fork
git clone https://github.com/keerthi-180205/neuroshell.git

# 3. Create a feature branch off dev
git checkout -b feature/your-feature-name dev

# 4. Make your changes

# 5. Commit using Conventional Commits
git commit -m "feat(parser): add 'define' intent detection"

# 6. Push and open a PR → targeting the dev branch
git push origin feature/your-feature-name
```

### Contribution Areas

- 🐛 **Bug Reports** — Found something broken? Open an issue.
- 💡 **Feature Ideas** — Have an idea for v0.2 or v0.3? Open a discussion.
- 📖 **Documentation** — Improve clarity, fix typos, add examples.
- 🔌 **Plugin Ideas** — Designing a future NeuroPlugin? Share the concept.

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before submitting a PR.

---

## 📄 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](./LICENSE) file for details.

You are free to use, modify, and distribute this software. If you build something with NeuroShell, a ⭐ star and a mention would mean the world.

---

## 👨‍💻 Author

**Keerthi** — Building NeuroLink OS, one phase at a time.

- GitHub: [@keerthi-180205](https://github.com/keerthi-180205)

---

<div align="center">

**If NeuroShell saved you time, gave you a spark, or just made you smile — drop a ⭐**

*The world needs NeuroLink. Let's build it together.*

<br/>

`Python` · `Ollama` · `Local AI` · `CLI` · `Open Source` · `NeuroLink OS`

</div>
