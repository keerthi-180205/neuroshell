# NeuroShell — Voice CLI interface
# Handles microphone input and text output.
# Calls orchestrator.process() — exact same logic as text.py

# pyrefly: ignore [missing-import]
import speech_recognition as sr
import pyttsx3
import re
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from app.core.orchestrator import Orchestrator
from app.core.config import Config


class VoiceInterface:
    """Terminal-based voice interface for NeuroShell.
    
    This interface listens to the microphone, converts speech to text,
    and then sends that text to the same orchestrator used by the text interface.
    """

    def __init__(self):
        self.console = Console()
        self.orchestrator = Orchestrator()
        self.recognizer = sr.Recognizer()
        
        # We will use the default system microphone
        try:
            self.microphone = sr.Microphone()
        except OSError as e:
            self.console.print(f"[bold red]Microphone Error:[/bold red] Could not find a microphone. {e}")
            self.microphone = None
            
        # Initialize the Text-to-Speech engine
        try:
            self.tts_engine = pyttsx3.init()
            # Optional: Slow down the speech rate slightly for better clarity
            rate = self.tts_engine.getProperty('rate')
            self.tts_engine.setProperty('rate', rate - 20)
            
            # Configure female voice directly (espeak handles +f3 variants internally)
            target_voice = "gmw/en-us+f3"
            try:
                self.tts_engine.setProperty('voice', target_voice)
                self.console.print(f"[dim]TTS Voice initialized: {target_voice}[/dim]")
            except Exception:
                self.console.print("[dim]TTS Voice initialized: System Default[/dim]")
                
        except Exception as e:
            self.console.print(f"[bold red]TTS Error:[/bold red] Could not initialize text-to-speech. {e}")
            self.tts_engine = None

    def _show_banner(self) -> None:
        """Display the welcome banner at startup."""
        banner = Text()
        banner.append("🎙️ NeuroShell Voice", style="bold green")
        banner.append(f" v{Config.APP_VERSION}", style="dim")
        banner.append("\n")
        banner.append("Say ", style="dim")
        banner.append("'exit'", style="bold red")
        banner.append(" or ", style="dim")
        banner.append("'quit'", style="bold red")
        banner.append(" to stop.", style="dim")

        self.console.print()
        self.console.print(Panel(banner, border_style="bright_green"))
        self.console.print()

    def _show_response(self, response: str) -> None:
        """Display the assistant's response in the terminal and speak it."""
        self.console.print(f"\n[bold cyan]NeuroShell:[/bold cyan] {response}\n")
        
        # Speak the response if the TTS engine is available
        if self.tts_engine:
            # Strip markdown characters (*, _, #, `) before speaking so it sounds natural
            clean_text = re.sub(r'[*_#`]', '', response)
            self.tts_engine.say(clean_text)
            self.tts_engine.runAndWait()

    def _listen(self) -> str:
        """Listen to the microphone and convert speech to text."""
        if not self.microphone:
            return ""

        with self.microphone as source:
            self.console.print("[dim]Adjusting for ambient noise...[/dim]")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            self.console.print("\n[bold green]🎙️ Listening... (speak now)[/bold green]")
            try:
                # Listen for audio input from the user
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                self.console.print("[dim]Processing speech...[/dim]")
                # Use Google's free Web Speech API to convert to text
                text = self.recognizer.recognize_google(audio)
                
                self.console.print(f"[bold yellow]You said:[/bold yellow] {text}")
                return text
                
            except sr.WaitTimeoutError:
                self.console.print("[dim]No speech detected.[/dim]")
                return ""
            except sr.UnknownValueError:
                self.console.print("[dim]Could not understand audio.[/dim]")
                return ""
            except sr.RequestError as e:
                self.console.print(f"[bold red]API Error:[/bold red] {e}")
                return ""
            except (KeyboardInterrupt, EOFError):
                return "exit"

    def start(self) -> None:
        """Start the interactive voice conversation loop."""
        self._show_banner()
        
        if not self.microphone:
            self.console.print("[bold red]Cannot start voice interface without a microphone.[/bold red]")
            return

        while True:
            user_input = self._listen()

            # Exit commands
            if user_input.strip().lower() in ("exit", "quit"):
                self.console.print(
                    "\n[bold magenta]👋 Goodbye! NeuroShell Voice shutting down.[/bold magenta]\n"
                )
                break

            # Skip empty input (like when nothing is heard)
            if not user_input.strip():
                continue

            # Send the transcribed text to the orchestrator!
            self.console.print("[dim]Thinking...[/dim]")
            response = self.orchestrator.process(user_input)
            self._show_response(response)
