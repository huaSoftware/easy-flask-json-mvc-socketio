'''
@Author: hua
@Date: 2018-08-30 10:52:11
@description: 
@LastEditors: hua
@LastEditTime: 2019-11-28 20:33:49
'''
import os,json
path = os.getcwd()+'/.runtime/environment.json'
data = {"environment":"socket"}
with open(path, "w") as f:
    f.write(json.dumps(data))
    
from app import app, socketio
from flask_cors import CORS
# https://www.cnblogs.com/franknihao/p/7202253.html uwsgi配置
app = app
CORS(app, supports_credentials=True)
if __name__ == '__main__':
    app.debug = False
    socketio.run(app, host='0.0.0.0', port=501)