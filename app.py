import json
from sarufi import Sarufi

sarufi = Sarufi("prosper", "3102")

chatbot = sarufi.get_bot(23)

chatbot.intents = json.load(open("intents.json"))

chatbot.flow = json.load(open("flow.json"))

def chat():
    while True:
        message = input("Me : ")
        response = sarufi.chat(bot_id=23, chat_id="furaha", message=message)
        print(f"Bot: {response}")


def respond(message, chat_id):
    response = sarufi.chat(bot_id=23, chat_id=chat_id, message=message)
    return response.get("message")


if __name__ == "__main__":
    chat()