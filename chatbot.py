import sys

def chatbot():
    print("Chatbot: Hello! I am a simple rule-based AI. (Type 'quit', 'exit', or 'bye' to stop)")
    print("-" * 60)

    while True:
        # 1. Get input from the user and clean it up
        user_input = input("You: ").strip().lower()

        # 2. Check for exit commands
        if user_input in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # 3. Rule Matching using if-elif-else
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hey there! How can I help you today?")
            
        elif "your name" in user_input:
            print("Chatbot: I'm QuickBot, a simple rule-based chatbot.")
            
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm functioning perfectly! How are you?")
            
        elif "weather" in user_input:
            print("Chatbot: I don't have real-time internet access, but I hope it's sunny where you are!")
            
        elif "help" in user_input:
            print("Chatbot: I can answer basic questions about myself, the weather, or just say hello!")
            
        # 4. Fallback response for unknown queries
        else:
            print("Chatbot: I'm sorry, I didn't quite catch that. Could you rephrase or type 'help'?")
            
        print() # Adds a blank line for readability

if __name__ == "__main__":
    chatbot()