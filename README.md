<div align="center">

![NeuroShell](https://img.shields.io/badge/NeuroShell-v0.1.0-8A2BE2?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

<pre>
 _   _                      ____  _          _ _ 
| \ | |                    / ___|| |__   ___| | |
|  \| | ___ _   _ _ __ ___ \___ \| '_ \ / _ \ | |
| . ` |/ _ \ | | | '__/ _ \ ___) | | | |  __/ | |
| |\  |  __/ |_| | | | (_) |____/|_| |_|\___|_|_|
|_| \_|\___|\__,_|_|  \___/                       
</pre>

### 🧠 The AI-powered CLI that understands you. *(In Development)*

**The foundation of NeuroLink OS.**

[Getting Started](#-getting-started) · [Features](#-features) · [Usage](#-usage) · [Roadmap](#-roadmap) · [Contributing](#-contributing)

</div>

---

NeuroShell isn't a chatbot wrapper or a "Jarvis clone." It's built in three deliberate stages:

- **V1 — Understand Me** *(this repo, in progress)*
- **V2 — Control My Computer**
- **V3 — Help Me Accomplish My Goals**

V1 focuses on getting the foundation right: natural conversation, explicit long-term memory, personal knowledge retrieval (RAG), a small set of safe tools, read-only Linux system awareness, and voice I/O — all behind clean, swappable interfaces.

```
You:        "Hey NeuroShell."
NeuroShell: "Hey! What's up?"

You:        "Remember that I'm working on NeuroShell, my AI assistant."
NeuroShell: "Got it — I'll remember that."

You:        "How much RAM am I using?"
NeuroShell: "9.8 GB out of 16 GB. Chrome, VS Code, and Python are your top consumers."

You:        "Read my ML notes and explain regularization."
NeuroShell: "Sure — your notes describe regularization as..."
```

---

## ✨ Features

- 💬 **Conversation engine** — session history, context management, automatic summarization when history grows
- 🧠 **Explicit long-term memory** — NeuroShell only remembers what you tell it to (`remember`, `forget`, `what do you remember about me`, `delete all my memories`)
- 📚 **Personal knowledge / RAG** — ingest PDFs, Markdown, TXT, DOCX; answers cite their source
- 🛠️ **Safe tool calling** — calculator, time/date, weather, web search
- 🐧 **Read-only Linux system awareness** — CPU, RAM, disk, GPU, processes, OS info (via `psutil`)
- 🎙️ **Voice I/O** — faster-whisper (STT) + Piper (TTS), fully optional; text/CLI always works
- 🔒 **Permission system** — 6 levels (0–5); V1 only ever operates at levels 0–2
- 📝 **Audit logging** — every tool call, permission decision, and memory change is logged
- 🔌 **Provider-agnostic LLM layer** — cloud (OpenAI-compatible) or local (Ollama), swap without touching the rest of the app

### What V1 deliberately excludes

No arbitrary shell execution, no root/sudo access, no autonomous or destructive actions, no multi-agent orchestration, no GUI. Those are V2/V3 territory — see [Roadmap](#-roadmap).

---

## 🏗️ Architecture

```
User (text/voice)
      │
Input Processing
      │
Context Manager ── Memory Retrieval ── Knowledge Retrieval (RAG)
      │
   AI Brain (LLM abstraction)
      │
Intent / Tool Decision
      │
Tool Router ── Permission Layer ── Tool Execution
      │
Response Generation ── Memory Update (if applicable)
      │
Output (text/voice)
```

Every external dependency — LLM provider, embeddings, STT, TTS — sits behind an interface. The core never imports a provider SDK directly.

---

## 🧰 Tech stack

| Layer | Choice | Why |
|---|---|---|
| Language | Python 3.11+ | typed, async where it matters |
| LLM | Provider-agnostic (OpenAI-compatible cloud / Ollama local) | no vendor lock-in |
| Database | PostgreSQL + pgvector | one store for relational + vector data |
| Migrations | Alembic | reproducible schema |
| STT | faster-whisper | fast, local-capable |
| TTS | Piper | lightweight, local |
| Wake word | openWakeWord (optional) | opt-in, not required |
| CLI | Rich | polished terminal UX without a GUI |
| Testing | pytest + mocks | no real API calls in test suite |
| Infra (dev) | Docker Compose (Postgres/pgvector only) | voice & system tools run on host |

No LangChain, LangGraph, CrewAI, or AutoGen — the architecture is intentionally explicit so the internals stay understandable.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Docker (for Postgres + pgvector)
- An LLM provider API key, or a local [Ollama](https://ollama.ai) install

### Installation

```bash
git clone https://github.com/keerthi-180205/neuroshell.git
cd neuroshell
python -m venv venv && source venv/bin/activate
pip install -e .
cp .env.example .env        # add your LLM provider key, DB URL, etc.
docker compose up -d        # starts Postgres + pgvector
neuroshell db upgrade       # run migrations
```

---

## 🖥️ Usage

```bash
neuroshell chat        # start a text conversation
neuroshell voice        # start voice mode
neuroshell memory       # inspect/manage long-term memory
neuroshell knowledge    # manage the RAG knowledge base
neuroshell system       # query Linux system info directly
neuroshell config       # view/edit configuration
neuroshell doctor       # check environment health
```

---

## ⚙️ Configuration

All behavior is config-driven — see `config/neuroshell.yaml` and `.env.example`. Key sections:

```yaml
llm:
  provider: openai_compatible   # or: ollama
  model: <model-name>

personality:
  name: NeuroShell
  style: friendly
  humor: moderate
  verbosity: balanced

voice:
  enabled: false
  stt: faster-whisper
  tts: piper
  wake_word: false

security:
  max_permission_level: 2   # V1 hard ceiling
```

---

## 🔒 Security Model

| Level | Scope | Enabled in V1 |
|---|---|---|
| 0 | Conversation only | ✅ |
| 1 | Read-only information | ✅ |
| 2 | Safe local tools | ✅ |
| 3 | File modification | ❌ (V2) |
| 4 | System modification | ❌ (V2) |
| 5 | Administrative/root | ❌ (V3, if ever) |

The LLM never receives unrestricted shell access, root privileges, or secrets it doesn't need. Every tool call and permission decision is audit-logged.

---

## 🔐 Privacy

NeuroShell is local-first where it can be:

- **Stays local**: system info, database, memory, local documents, voice (when using local STT/TTS)
- **Leaves the machine**: cloud LLM calls, cloud web search, any other external API you enable

You always know what's local vs. cloud from the config file.

---

## 🗺️ Roadmap

- [x] V1 — Understand Me: conversation, memory, RAG, safe tools, read-only system info, voice
- [ ] V2 — Control My Computer: supervised file/system modification, broader automation
- [ ] V3 — Help Me Accomplish My Goals: goal-directed assistance, plugin ecosystem (GitHub, calendar, Docker, etc.)

V1 milestones are tracked in [`docs/milestones.md`](docs/milestones.md).

---

## 🤝 Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for dev setup, code style, and how to add a new tool. The tool interface is designed to be plugin-ready — see `docs/adding-tools.md`.

---

## 📄 License

Licensed under the [Apache License 2.0](LICENSE).

---

## ⚠️ Disclaimer

NeuroShell can read system state and call external APIs on your behalf. Review `config/neuroshell.yaml` before enabling voice or web access, and never commit `.env`, API keys, or personal knowledge-base documents to the repo.
