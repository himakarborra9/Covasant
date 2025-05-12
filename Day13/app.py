from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

MISTRAL_API_KEY = 'JPBcoWLoAm12M5R0hmIxmhEhdyijVQ3K'

chat_history = []

@app.route('/chat', methods=['POST'])
def chat():
    global chat_history
    user_msg = request.json['message']

    if not chat_history:
        chat_history = []

    chat_history.append({"role": "user", "content": user_msg})

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-large-latest",
        "messages": chat_history
    }

    response = requests.post("https://api.mistral.ai/v1/chat/completions", headers=headers, json=payload)
    reply = response.json()['choices'][0]['message']['content']
    chat_history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply, "history": chat_history})


@app.route('/clear', methods=['POST'])
def clear_history():
    global chat_history
    chat_history = []  
    return jsonify({"status": "cleared"})


if __name__ == '__main__':
    app.run()