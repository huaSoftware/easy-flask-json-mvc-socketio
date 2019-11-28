'''
@Author: hua
@Date: 2018-08-30 10:52:11
@description: 
@LastEditors: hua
@LastEditTime: 2019-11-28 20:33:34
'''
import os,json
path = os.getcwd()+'/.runtime/environment.json'
data = {"environment":"restful"}
with open(path, "w") as f:
    f.write(json.dumps(data))
    
from app import app
from flask_restful import Api
from flask_cors import CORS
from app.Controllers.RestfulController import TodoList
# https://www.cnblogs.com/franknihao/p/7202253.html uwsgi配置
#https://www.jianshu.com/p/ed1f819a7b58 restful配置
api = Api(app)
api.add_resource(TodoList, '/todos')
app = app
CORS(app, supports_credentials=True)
if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=502)
