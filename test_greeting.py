from app.core.orchestrator import Orchestrator

def main():
    print("Initializing Orchestrator for test...")
    orchestrator = Orchestrator()
    
    test_inputs = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "what is machine learning?"
    ]
    
    print("====================================")
    for user_input in test_inputs:
        print(f"\nUser: {user_input}")
        response = orchestrator.process(user_input)
        print(f"NeuroShell: {response}")
        print("====================================")

if __name__ == "__main__":
    main()
