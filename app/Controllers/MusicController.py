''' 
    author:hua
    Music Spider
    data:2017/12/2
'''
from app import app
from app.Models.Music import Music
from app.Controllers.Controller import Controller
from flask import request

''' 测试接口 '''


@app.route('test', methods=['GET'])
def index():

    

''' 歌曲名字 '''


@app.route('/api.v1/music.index', methods=['GET'])
def music_index():
    if 'id' in request.args:
        mus = Music.song_name(request.args['id'])
    else:
        return Controller.error()
    return Controller.successData(mus)


''' 歌曲结果 '''


@app.route('/api.v1/music.result', methods=['GET'])
def music_result():
    if 'id' in request.args:
        res = Music.music_name(request.args['id'])
    else:
        return Controller.error()
    return Controller.successData(res)


''' 歌曲名字非中文 '''


@app.route('/api.v1/music.audio', methods=['GET'])
def music_audio():
    if 'name' in request.args:
        aud = Music.song(request.args['name'])
    else:
        return Controller.error()
    return Controller.successData(aud)
