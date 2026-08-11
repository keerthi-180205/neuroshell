# NeuroShell — Text CLI interface
# Handles terminal input/output ONLY. No LLM logic here.
# Calls orchestrator.process() — same method voice.py will call later.

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from app.core.orchestrator import Orchestrator
from app.core.config import Config


class TextInterface:
    """Terminal-based text interface for NeuroShell.
    
    This is an interface — it handles HOW the user interacts.
    The orchestrator handles WHAT happens with the input.
    
    A future voice.py will be another interface calling the
    same orchestrator. Same brain, different mouth.
    """

    def __init__(self):
        self.console = Console()
        self.orchestrator = Orchestrator()

    def _show_banner(self) -> None:
        """Display the welcome banner at startup."""
        banner = Text()
        banner.append("🧠 NeuroShell", style="bold magenta")
        banner.append(f" v{Config.APP_VERSION}", style="dim")
        banner.append("\n")
        banner.append("Type your message. Type ", style="dim")
        banner.append("exit", style="bold red")
        banner.append(" to quit.", style="dim")

        self.console.print()
        self.console.print(Panel(banner, border_style="bright_magenta"))
        self.console.print()

    def _show_response(self, response: str) -> None:
        """Display the assistant's response."""
        self.console.print(f"\n[bold cyan]NeuroShell:[/bold cyan] {response}\n")

    def _get_input(self) -> str:
        """Get user input from terminal."""
        try:
            return self.console.input("[bold green]You:[/bold green] ")
        except (EOFError, KeyboardInterrupt):
            return "exit"

    def start(self) -> None:
        """Start the interactive conversation loop.
        
        Loop: get input → send to orchestrator → show response → repeat
        Exit on 'exit', 'quit', or Ctrl+C
        """
        self._show_banner()

        while True:
            user_input = self._get_input()

            # Exit commands
            if user_input.strip().lower() in ("exit", "quit"):
                self.console.print(
                    "\n[bold magenta]👋 Goodbye! NeuroShell shutting down.[/bold magenta]\n"
                )
                break

            # Skip empty input
            if not user_input.strip():
                continue

            # Send to orchestrator, display response
            response = self.orchestrator.process(user_input)
            self._show_response(response)
