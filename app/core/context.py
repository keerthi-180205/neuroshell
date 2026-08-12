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

    def add_message(self, role: str, content: str, name: str = None, args: dict = None, raw_part=None) -> None:
        """Add a message to conversation history.
        
        Args:
            role: "user", "assistant", "tool_call", or "tool_result"
            content: The message text
            name: The name of the tool (if applicable)
            args: The tool arguments (if applicable)
            raw_part: The raw API object (if applicable)
        """
        if role not in ("user", "assistant", "tool_call", "tool_result"):
            raise ValueError(f"Invalid role: {role}. Must be 'user', 'assistant', 'tool_call', or 'tool_result'.")
            
        message = {"role": role, "content": content}
        if name:
            message["name"] = name
        if args is not None:
            message["args"] = args
        if raw_part is not None:
            message["raw_part"] = raw_part
            
        self._history.append(message)

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
