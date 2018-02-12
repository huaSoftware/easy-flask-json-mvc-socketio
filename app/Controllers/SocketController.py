from flask_socketio import emit, join_room, leave_room
from app import socketio
from flask import session
from threading import Lock

thread = None
thread_lock = Lock()


def background_thread():
    """Example of how to send server generated events to clients.
       增加一个线程处理后台程序，这里需要自己设置条件关闭，或者一直作为生产者
       每次返回消息会增加一个线程，这个还需要看下websocket底层实现
    """
    count = 0
    while True:
        socketio.sleep(1)
        count += 1
        socketio.emit(
            'my_request', {'data': 'Server generated event',
                           'count': count},
            namespace='/test')


''' 后台异步执行推送
    对应view层的system_response.html 
'''


@socketio.on('my_request', namespace='/test')
def test_connect(message):
    value = message.get('param')
    print(value)
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(
                target=background_thread)
    emit('my_request', {'data': 'Connected', 'count': 0})


@socketio.on('request_for_response', namespace='/test')
def give_response(message):
    value = message.get('param')
    print(value)


''' 全局广播，不加只是单个页面通信,
    对应view层的my_broadcast_eventA,B.html
'''


@socketio.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit(
        'my_broadcast_event',
        {'msg': message['data'],
         'count': session['receive_count']},
        broadcast=True)


''' 聊天室模式，进入，离开，聊天
    对应view层的chatRoom1_A,B.html，客户端可以设置房间号，用来区分响应作用域
 '''


@socketio.on('join', namespace='/test')
def join(message):
    room = message['room']
    join_room(room)
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit(
        'join',
        {'room': 'Welcome to: ' + room,
         'count': session['receive_count']},
        room=room)


@socketio.on('leave', namespace='/test')
def leave(message):
    room = message['room']
    leave_room(room)
    emit('leave', {'room': 'leave up: '+room}, room=room)


@socketio.on('chat', namespace='/test')
def chat(message):
    emit('chat', {'data': message['msg']}, room=message['room'])
