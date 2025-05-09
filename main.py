import os
from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO, emit
from core.logic import get_bot_response

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
socket_io = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "ZarickAI Backend is running!"

@socket_io.on('message')
def handle_message(data):
    message = data.get("message", data) if isinstance(data, dict) else data

    bot_response = get_bot_response(message)
    emit("response", {"message": bot_response})
    
if __name__ == '__main__':
    socket_io.run(app, host='0.0.0.0', port=5000)
