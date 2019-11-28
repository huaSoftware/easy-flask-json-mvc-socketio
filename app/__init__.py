'''
@Author: hua
@Date: 2018-08-30 10:52:23
@LastEditors: hua
@LastEditTime: 2019-11-28 20:32:43
'''
from flask import Flask
#权限模块 https://github.com/raddevon/flask-permissions
#from flask_permissions.core import Permissions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_socketio import SocketIO
from app.Vendor.Code import Code
from app.env import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, UPLOAD_FOLDER, MAX_CONTENT_LENGTH
import os, json

#读取启动环境
with open(os.getcwd()+'/.runtime/environment.json', "r") as f:
    environment = json.loads(f.read())['environment']
    
#普通json带error_code风格使用此app示例
app = Flask(__name__)
#注册权限
#perms = Permissions(app, db, None)
# 实例化websocket
async_mode = 'gevent'
socketio = SocketIO(app, async_mode=async_mode)
# 配置 sqlalchemy  数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
#上传文件配置
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #上传目录 
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH #上传大小
#创建数据库及连接
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
dBSession = DBSession()

from app.Vendor.ExceptionApi import ExceptionApi
@app.teardown_appcontext
def shutdown_session(exception=None):
    dBSession.close()
    
#挂载500异常处理,并记录日志
if environment == 'run' or environment == 'restful':
    @app.errorhandler(Exception)
    def error_handler(e):
        return ExceptionApi(Code.ERROR, e)

if environment == 'socket':
    @socketio.on_error_default       # Handles the default namespace
    def error_handler(e):
        return ExceptionApi(Code.ERROR, e)
#引入使用的控制器
if environment == 'run' or environment == 'restful':
    from app.Controllers import  UsersController, RestfulController, AdminController
    # 蓝图，新增的后台部分代码
    from app.Controllers.AdminController import admin
    app.register_blueprint(admin, url_prefix='/admin')
if environment == 'socket':
    #引入socketio控制层
    from app.Controllers import SocketController
