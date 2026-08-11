# NeuroShell — Orchestrator (the central coordinator)
# This is NOT an AI model. It's Python code that coordinates:
#   User input → Context → LLM → Response
# In Stage 2, it will also coordinate tools.

from app.core.config import Config
from app.core.llm import LLMClient
from app.core.context import ConversationContext
from app.prompts.system_prompt import SYSTEM_PROMPT


class Orchestrator:
    """Central coordinator of the NeuroShell system.
    
    Receives user input from any interface (text, voice in future),
    manages context, communicates with the LLM, and returns responses.
    
    Stage 1 flow:
        user_input → add to context → LLM(system_prompt + history) → response → add to context
    
    Stage 2 will add:
        → tool detection → tool execution → result back to LLM
    """

    def __init__(self):
        """Initialize orchestrator: validate config, create LLM and context."""
        Config.validate()  # Fail fast if config is wrong
        self.llm = LLMClient()
        self.context = ConversationContext()

    def process(self, user_input: str) -> str:
        """Process a user message and return the assistant's response.
        
        This is the ONLY method interfaces need to call.
        text.py calls it. voice.py will call it too. Same method, same brain.
        
        Args:
            user_input: What the user said/typed.
        
        Returns:
            The assistant's response string.
        """
        # Guard: empty input
        if not user_input or not user_input.strip():
            return "I didn't catch that. Could you say something?"

        # Step 1: Record user message in context
        self.context.add_message("user", user_input.strip())

        # Step 2: Send full context + system prompt to LLM
        try:
            response = self.llm.generate(
                system_prompt=SYSTEM_PROMPT,
                conversation_history=self.context.get_history(),
            )
        except ConnectionError as e:
            return f"⚠️ Connection issue: {e}"
        except Exception as e:
            return f"⚠️ Something went wrong: {e}"

        # Step 3: Record assistant response in context
        self.context.add_message("assistant", response)

        # Step 4: Return to the interface
        return response
