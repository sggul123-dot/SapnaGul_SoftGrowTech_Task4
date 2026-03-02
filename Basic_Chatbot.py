class BasicChatbot:
    def get_response(self, user_input):
        if user_input == "hello":
            return "Hi!"
        elif user_input == "how are you":
            return "I'm fine, thanks!"
        elif user_input == "bye":
            return "Goodbye!"
        else:
            return "I don't understand that."

    def run(self):
        print("Simple Chatbot (type 'bye' to exit)")
        
        while True:
            user_input = input("You: ").lower()
            response = self.get_response(user_input)
            print("Bot:", response)

            if user_input == "bye":
                break


if __name__ == "__main__":
    chatbot = BasicChatbot()
    chatbot.run()