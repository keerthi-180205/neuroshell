#!/usr/bin/env python3
# NeuroShell — Voice Entry Point

import sys
import os

# Ensure the app module can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.interfaces.voice import VoiceInterface

if __name__ == "__main__":
    try:
        app = VoiceInterface()
        app.start()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
