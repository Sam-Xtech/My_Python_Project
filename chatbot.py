import nltk
from nltk.stem import PorterStemmer

# Download NLTK tokenizer (run only once)
nltk.download("punkt_tab")

stemmer = PorterStemmer()

# --- Knowledge Base ---
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How may I help you?",
    "order": "You can track your order using your order ID on our website.",
    "refund": "To request a refund, please visit the returns section or contact customer care.",
    "return": "You can initiate a return within 7 days of delivery.",
    "payment": "We support UPI, Net Banking, Debit/Credit Cards, and Wallets.",
    "shipping": "Shipping usually takes 3–5 business days.",
    "delivery": "Your package will be delivered based on the shipping speed you selected.",
    "contact": "You can reach customer support at support@example.com.",
    "help": "Sure! Tell me how I can help you."
}

# --- Preprocessing function ---
def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    stems = [stemmer.stem(word) for word in tokens]
    return stems

# --- Chatbot logic ---
def chatbot_reply(user_input):
    stems = preprocess(user_input)

    for keyword in responses:
        if stemmer.stem(keyword) in stems:
            return responses[keyword]

    return "I'm sorry, I didn't understand that. Could you rephrase your question?"

# --- Chat Loop ---
print("🤖 Customer Service Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Thank you for chatting! Have a great day!")
        break

    reply = chatbot_reply(user_input)
    print("Bot:", reply)
