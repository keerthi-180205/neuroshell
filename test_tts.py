import pyttsx3
import time

def main():
    print("Testing Voice Interface Initialization...")
    
    # 1. Init engine
    engine = pyttsx3.init()
    
    # 2. Check for voice
    target_voice_id = "english-us+f3"
    voice_found = False
    
    for voice in engine.getProperty('voices'):
        if target_voice_id in voice.id:
            engine.setProperty('voice', voice.id)
            print(f"TTS Voice initialized: {voice.id}")
            voice_found = True
            break
            
    if not voice_found:
        print(f"TTS Voice initialized: System Default (Target '{target_voice_id}' not found)")
        
    print("\nNeuroShell: Hello! I am NeuroShell. How can I help you?")
    engine.say("Hello! I am NeuroShell. How can I help you?")
    engine.runAndWait()

if __name__ == "__main__":
    main()
