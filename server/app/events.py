from flask import request
from flask_socketio import emit,join_room

from .extensions import socketio

# Mudar para DB
sessions = {}

#Create session
def create_session(uuid):
    user_id = uuid
    sessions[user_id] = {"connected_users": []}
    print(sessions)

#Join session (this is for the main page and the controller)
@socketio.on('join_session')
def join_session(data):
    session_id = data.get('uuid')
    user = data.get('user')

    if session_id in sessions:
        join_room(session_id)
        sessions[session_id]['connected_users'].append(user)
        emit('user_connected', {'user': user}, room=session_id)
        print(sessions)
    else:
        emit('error', {'message': 'Sessão inválida'})

#Send messages (The controller to the main page)
@socketio.on('handle_message')
def handle_message(data):
    session_id = data.get('session_id')
    message = data.get('message')

    if session_id in sessions:
        emit('new_message', {'message': message}, room=session_id)
    else:
        emit('error', {'message': 'Sessão inválida'})