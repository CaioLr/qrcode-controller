from flask import request
from flask_socketio import emit,join_room

from .extensions import socketio

# Use your own DB, to keep the sessions and user connected
sessions = {}

#Create session
def create_session(uuid):
    sessions[str(uuid)] = {"connected_users": []}
    print(sessions)

#Join session (this is for the main page and the controller)
@socketio.on('join_session')
def join_session(data):

    print('Join session called')

    session_id = data.get('uuid')
    user = data.get('user')

    if session_id in sessions:
        join_room(session_id)
        sessions[session_id]['connected_users'].append(user)
        emit('user_connected', {'user': user}, room=session_id)
        print(sessions)
    else:
        emit('error', {'message': 'Sessão inválida'})
        print('ERROR')

#Send messages (The controller to the main page)
@socketio.on('handle_message')
def handle_message(data):
    session_id = data.get('session_id')
    message = data.get('message')

    if session_id in sessions:
        emit('new_message', {'message': message}, room=session_id, broadcast=True)
    else:
        emit('error', {'message': 'Sessão inválida'})