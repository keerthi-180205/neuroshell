import pyttsx3

def main():
    print("=====================================")
    print("AVAILABLE VOICES ON YOUR SYSTEM:")
    print("=====================================")
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    for v in voices:
        print(f"ID: {v.id}")
        
    print("=====================================")
    
if __name__ == "__main__":
    main()
