# Tests for ConversationContext

from app.core.context import ConversationContext
import pytest

def test_empty_context():
    """A new context should start empty."""
    ctx = ConversationContext()
    assert ctx.get_message_count() == 0
    assert ctx.get_history() == []

def test_add_user_message():
    """Adding a user message should store it correctly."""
    ctx = ConversationContext()
    ctx.add_message("user", "Hello Jarvis")
    
    history = ctx.get_history()
    assert ctx.get_message_count() == 1
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "Hello Jarvis"

def test_add_assistant_message():
    """Adding an assistant message should store it correctly."""
    ctx = ConversationContext()
    ctx.add_message("assistant", "How can I help?")
    
    history = ctx.get_history()
    assert ctx.get_message_count() == 1
    assert history[0]["role"] == "assistant"
    assert history[0]["content"] == "How can I help?"

def test_invalid_role_raises_error():
    """Adding a message with an invalid role should fail fast."""
    ctx = ConversationContext()
    
    # pytest.raises checks that the code inside the block throws a ValueError
    with pytest.raises(ValueError) as excinfo:
        ctx.add_message("system", "This should crash")
    
    assert "Invalid role" in str(excinfo.value)

def test_history_is_isolated():
    """External code should not be able to modify the internal history."""
    ctx = ConversationContext()
    ctx.add_message("user", "Secret")
    
    # Get a copy of the history and try to tamper with it
    history_copy = ctx.get_history()
    history_copy.append({"role": "user", "content": "Tampered"})
    
    # The actual context should remain unchanged
    assert ctx.get_message_count() == 1
    assert ctx.get_history()[0]["content"] == "Secret"

def test_clear_context():
    """Clearing the context should remove all messages."""
    ctx = ConversationContext()
    ctx.add_message("user", "Hello")
    ctx.add_message("assistant", "Hi")
    
    assert ctx.get_message_count() == 2
    ctx.clear()
    assert ctx.get_message_count() == 0
    assert ctx.get_history() == []
