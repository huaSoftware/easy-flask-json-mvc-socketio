import json
import requests
import re
import base64
from app import db
from app.Models.BaseModel import BaseModel


class Music(BaseModel, db.Model):
    __tablename__ = 'music'
    id = db.Column(db.Integer, primary_key=True)
    add_time = db.Column(db.Integer)
    content = db.Column(db.String(5000))

    def __init__(self, content, add_time):
        self.content = content
        self.add_time = add_time

    @staticmethod
    def music_name(name):
        url = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery191034642999175022426_1489023388639&keyword=%s&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1489023388641' % (
            name)

        headers = {
            'Host':
            'songsearch.kugou.com',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
            'Accept':
            '*/*',
            'Accept-Language':
            'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding':
            'gzip, deflate',
            'Referer':
            'http://www.kugou.com/yy/html/search.html',
            'Cookie':
            'kg_mid=3af81d5237db90c04a517a5dc12ef8ee; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1497918589; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1497934809',
            'Connection':
            'keep-alive'
        }
        r = requests.get(url, headers=headers)
        response = r.text
        matchObj = re.search(r'jQuery191034642999175022426_1489023388639(.*)',
                             response, re.M | re.I)
        content = json.loads(matchObj.group(1).strip('()'))
        html = ''
        for i in range(0, len(content['data']["lists"])):
            try:
                html = html + '''<div class= 'music'>
				            <a  href = 'musicAudio.html?name=%s'>%s</a>
				            <span> %s </span>
			              </div>
			           ''' % (content["data"]["lists"][i]["FileHash"],
                        content["data"]["lists"][i]["SongName"],
                        content["data"]["lists"][i]["SingerName"])
            except:
                return '''<div class="result-fail hidden" id="fail" style="display: block;">
                            <i class="icon iconfont icon-meiyoudingdan-01"></i>
                            <p>搜索如果没有结果</p>
                            <p>请核对您的歌曲名是否正确</p>
                        </div>'''
        return html

    @staticmethod
    def song_name(name):
        url = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery191034642999175022426_1489023388639&keyword=%s&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1489023388641' % (
            name)
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        response = r.text
        matchObj = re.search(r'jQuery191034642999175022426_1489023388639(.*)',
                             response, re.M | re.I)
        content = matchObj.group(1).strip('()')
        content = json.loads(content)
        if(len(content["data"]["lists"]) == 0):
            return 'error'
        url_parse = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash=' + content["data"]["lists"][0]["FileHash"]
        r_parse = requests.get(url_parse, headers=headers)
        response = json.loads(r_parse.text)
        data = '''
        <div id='jpg_div'>
              
            <div id='jpg'>%s
            </div>
		
        <div id="audio_name">%s
        </div>
         
	<div id='geci'>%s</div>
        <div id ="play">
            <div id='audio' >%s</div>
        </div>
        </div>
        ''' % (base64.b64encode(response['data']['img'].encode('utf8')),
               response['data']['audio_name'],
               base64.b64encode(response['data']['lyrics'].encode('utf8')),
               base64.b64encode(response['data']['play_url'].encode('utf8')))
        try:
            return data
        except:
            return 'error'

    @staticmethod
    def song(id_name):
        array_json = "44D1C80714260F96C902D0A4599D6B32"
        url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash=' + id_name
        headers = {
            'Host':
            'www.kugou.com',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
            'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':
            'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding':
            'gzip, deflate',
            'Cookie':
            'kg_mid=3af81d5237db90c04a517a5dc12ef8ee; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1497918589; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1497934809',
            'Connection':
            'keep-alive',
            'Upgrade-Insecure-Requests':
            '1',
        }
        r = requests.get(url, headers=headers)
        response = json.loads(r.text)
        data = '''
        <div id='jpg_div'>
              
            <div id='jpg'>%s
            </div>
		
        <div id="audio_name">%s
        </div>
         
	<div id='geci'>%s</div>
        <div id ="play">
            <div id='audio' >%s</div>
        </div>
        </div>
        ''' % (base64.b64encode(response['data']['img'].encode('utf8')),
               response['data']['audio_name'],
               base64.b64encode(response['data']['lyrics'].encode('utf8')),
               base64.b64encode(response['data']['play_url'].encode('utf8')))
        try:
            return data
        except:
            return 'error'
