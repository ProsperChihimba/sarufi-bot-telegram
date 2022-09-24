import json
import requests
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
    if response['message'][0] == "Thank you, you will soon receive USSD push notification, please enter you password for making payment":
        url = "https://api.shoket.co/v1/charge/"

        payload = json.dumps({
        "amount": "5000",
        "customer_name": "John Doe",
        "email": "john@user.com",
        "number_used": message,
        "channel": "Tigo"
        })
        headers = {
        'Authorization': 'Bearer ',
        'Content-Type': 'application/json'
        }

        responseData = requests.request("POST", url, headers=headers, data=payload)

        print(responseData.text)

    return response['message'][0]


if __name__ == "__main__":
    chat()