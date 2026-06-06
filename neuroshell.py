while True:
    user_input = input("> ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting NeuroShell...")
        break

    print(f"[NeuroShell]: You said -> {user_input}")