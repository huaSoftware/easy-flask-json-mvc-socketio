''' 
    author:hua
    Music Spider
    data:2017/12/2
'''
from app import app
from app.Models.Music import Music
from app.Controllers.BaseController import BaseController
from flask import request

''' 测试接口 '''


@app.route('/test', methods=['GET'])
def index():
    rules = {
        'name': {'type': 'integer', 'minlength': 10, 'maxlength': 20}
    }
    error_msg = {
        'name': {
            'type': u'姓名必须是整形',
            'minlength': u'姓名必须大于10',
            'maxlength': u'姓名必须小于20'
        }
    }
    error = BaseController().validateInput(rules, error_msg)
    if(error is not True):
        return error
    return BaseController().successData()

''' 歌曲名字 '''


@app.route('/api.v1/music.index', methods=['GET'])
def music_index():
    if 'id' in request.args:
        mus = Music.song_name(request.args['id'])
    else:
        return BaseController.error()
    return BaseController.successData(mus)


''' 歌曲结果 '''


@app.route('/api.v1/music.result', methods=['GET'])
def music_result():
    if 'id' in request.args:
        res = Music.music_name(request.args['id'])
    else:
        return BaseController.error()
    return BaseController.successData(res)


''' 歌曲名字非中文 '''


@app.route('/api.v1/music.audio', methods=['GET'])
def music_audio():
    if 'name' in request.args:
        aud = Music.song(request.args['name'])
    else:
        return BaseController.error()
    return BaseController.successData(aud)
