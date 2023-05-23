from flask import Flask, render_template
from flask_socketio import SocketIO, send
import random
import string

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

@socketio.on('connect')
def handle_connect():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    send(username)

if __name__ == '__main__':
    socketio.run(app)
