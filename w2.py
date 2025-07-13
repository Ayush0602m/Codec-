import random

responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! Need assistance?"],
    "goodbye": ["Goodbye! Have a nice day!", "See you again!"],
    "hours": ["Our working hours are 9 AM to 6 PM, Monday to Friday."],
    "pricing": ["We offer competitive pricing. Can you specify the product you're interested in?"],
    "default": ["I'm sorry, I didn't understand that. Can you please rephrase?"]
}


keywords = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"],
    "hours": ["hours", "open", "close", "timing", "time"],
    "pricing": ["price", "cost", "charge", "how much"]
}


def preprocess(sentence):
    # Lowercase and remove punctuation
    sentence = sentence.lower().replace("?", "").replace(".", "").replace(",", "")
    words = sentence.split()
    return words


def match_intent(user_input):
    words = preprocess(user_input)
    for intent, keys in keywords.items():
        if any(word in words for word in keys):
            return intent
    return "default"

def chatbot():
    print("🤖 Customer Service Bot: Hello! Ask me anything or type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("🤖 Bot: Goodbye!")
            break
        intent = match_intent(user_input)
        print("🤖 Bot:", random.choice(responses[intent]))

chatbot()
