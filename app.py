from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def chat():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    # with open('log.txt', 'a') as f:
    #     f.write(msg + '\n')
    emit('message', msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
