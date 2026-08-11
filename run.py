# NeuroShell — Entry point
# Run with: python run.py

from app.interfaces.text import TextInterface


def main():
    """Start NeuroShell."""
    try:
        interface = TextInterface()
        interface.start()

    except EnvironmentError as e:
        # Config validation failed (e.g., missing API key)
        print(f"\n❌ Configuration Error:\n{e}")
        print("\n💡 Fix: Add your GEMINI_API_KEY to the .env file.")

    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")

    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        raise  # Re-raise so you can see the full traceback during development


if __name__ == "__main__":
    main()
