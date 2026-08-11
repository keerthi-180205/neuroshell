# NeuroShell — Short-term conversation context
# Maintains message history for the current session only.
# This is NOT long-term memory — that comes in a future stage.


class ConversationContext:
    """Stores conversation history during a single session.
    
    Messages are stored in OUR universal format:
        {"role": "user" or "assistant", "content": "the message text"}
    
    Why our own format? Because Gemini uses "model" instead of "assistant",
    Ollama uses something else, etc. Our format is the standard —
    the LLM layer translates at the boundary.
    """

    def __init__(self):
        self._history: list[dict[str, str]] = []

    def add_message(self, role: str, content: str) -> None:
        """Add a message to conversation history.
        
        Args:
            role: "user" or "assistant"
            content: The message text
        """
        if role not in ("user", "assistant"):
            raise ValueError(f"Invalid role: {role}. Must be 'user' or 'assistant'.")
        self._history.append({"role": role, "content": content})

    def get_history(self) -> list[dict[str, str]]:
        """Return a COPY of the conversation history.
        
        Returns a copy so that external code can't accidentally
        modify our internal state.
        """
        return self._history.copy()

    def get_message_count(self) -> int:
        """Return how many messages are in history."""
        return len(self._history)

    def clear(self) -> None:
        """Clear all conversation history."""
        self._history = []
