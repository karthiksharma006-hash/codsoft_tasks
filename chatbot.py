
print("===================================")
print("       WELCOME TO AI CHATBOT")
print("===================================")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user_input:
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif "how are you" in user_input:
        print("Bot: I am fine. Thank you for asking!")

    elif "what can you do" in user_input:
        print("Bot: I can answer simple questions using predefined rules.")

    elif "python" in user_input:
        print("Bot: Python is a popular programming language.")

    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand. Please try another question.")
