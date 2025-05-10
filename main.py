import os
import eventlet
from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO, emit
from core.logic import get_bot_response

# Load environment variables
load_dotenv()

eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-secret-key")
socket_io = SocketIO(app, cors_allowed_origins=os.getenv("CORS_ALLOWED_ORIGINS", "*"))

@app.route('/')
def index():
    return "ZarickAI Backend is running!"

@socket_io.on('message')
def handle_message(data):
    try:
        message = data.get("message", data) if isinstance(data, dict) else data
        if not message or not isinstance(message, str):
            emit("error", {"message": "Invalid message format"})
            return

        bot_response = get_bot_response(message)
        emit("response", {"message": bot_response})
    except Exception as e:
        emit("error", {"message": "An error occurred while processing your message"})
        print(f"Error processing message: {str(e)}")
    
if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    socket_io.run(app, host='0.0.0.0', port=port)
