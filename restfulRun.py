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
