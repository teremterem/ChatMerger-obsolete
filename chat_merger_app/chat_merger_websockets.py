from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
socketio = SocketIO(app)


@app.route("/")
def index():
    return "Hello world!"


@socketio.on("join_room")
def on_join(data):
    room = data["room"]
    join_room(room)
    emit("room_message", f"has joined the room.", room=room)


@socketio.on("leave_room")
def on_leave(data):
    room = data["room"]
    leave_room(room)
    emit("room_message", f"has left the room.", room=room)


@socketio.on("send_message")
def on_send_message(data):
    room = data["room"]
    message = data["message"]
    emit("room_message", message, room=room)


if __name__ == "__main__":
    socketio.run(app)
