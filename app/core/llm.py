# NeuroShell — LLM abstraction layer
# Currently implements Google Gemini.
# The rest of the app calls THIS module — never Gemini directly.
# To swap LLMs later, only this file changes.

import google.generativeai as genai
from app.core.config import Config


class LLMClient:
    """Abstraction over the LLM provider.
    
    Currently uses Google Gemini. The orchestrator and other components
    call generate() without knowing which LLM is behind it.
    
    Translation happens here:
        Our format:    {"role": "assistant", "content": "..."}
        Gemini format: {"role": "model",     "parts": ["..."]}
    """

    def __init__(self):
        """Configure the Gemini SDK with the API key."""
        genai.configure(api_key=Config.GEMINI_API_KEY)

    def generate(self, system_prompt: str, conversation_history: list[dict]) -> str:
        """Generate a response given system prompt and conversation history.
        
        Args:
            system_prompt: Instructions defining assistant behavior.
            conversation_history: Messages in OUR format:
                [{"role": "user"/"assistant", "content": "..."}]
        
        Returns:
            The assistant's response as a string.
        
        Raises:
            ConnectionError: If the API is unreachable or key is invalid.
            ValueError: If the response is empty.
        """
        try:
            # Create model with system instruction
            model = genai.GenerativeModel(
                model_name=Config.GEMINI_MODEL,
                system_instruction=system_prompt,
            )

            # Convert OUR message format → Gemini's format
            gemini_contents = []
            for message in conversation_history:
                # Gemini uses "model" where we use "assistant"
                gemini_role = "model" if message["role"] == "assistant" else "user"
                gemini_contents.append({
                    "role": gemini_role,
                    "parts": [message["content"]],
                })

            # Send to Gemini and get response
            response = model.generate_content(gemini_contents)

            # Validate response
            if not response or not response.text:
                raise ValueError("LLM returned an empty response.")

            return response.text

        except ValueError:
            raise  # Re-raise our own ValueError
        except Exception as e:
            error_msg = str(e).lower()
            if "api key" in error_msg or "api_key" in error_msg:
                raise ConnectionError(f"Gemini API key error: {e}") from e
            elif "network" in error_msg or "connect" in error_msg:
                raise ConnectionError(f"Cannot reach Gemini API: {e}") from e
            else:
                raise RuntimeError(f"LLM error: {e}") from e
