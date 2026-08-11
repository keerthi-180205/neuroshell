# NeuroShell — Configuration loader
# Loads settings from .env file. Secrets never hardcoded.

import os
from dotenv import load_dotenv

# Load .env file into environment variables
load_dotenv()


class Config:
    """Central configuration for NeuroShell.
    
    All settings come from environment variables (.env file).
    This class reads them once and makes them available to the app.
    """

    # LLM Configuration
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

    # Application Identity
    APP_NAME: str = "NeuroShell"
    APP_VERSION: str = "0.1.0"

    @classmethod
    def validate(cls) -> None:
        """Check that all required config is present.
        
        Called once at startup. Fails fast with a clear error
        instead of crashing mid-conversation.
        """
        errors = []

        if not cls.GEMINI_API_KEY:
            errors.append("GEMINI_API_KEY is not set. Add it to your .env file.")

        if errors:
            raise EnvironmentError(
                "Configuration errors:\n" + "\n".join(f"  ✗ {e}" for e in errors)
            )
