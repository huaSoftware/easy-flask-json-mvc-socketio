from flask_socketio import emit
from app import socketio


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})