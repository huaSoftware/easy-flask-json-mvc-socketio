'''
@Author: hua
@Date: 2018-08-30 10:52:23
@LastEditors: hua
@LastEditTime: 2019-07-25 08:41:27
'''
from flask import Flask
#权限模块 https://github.com/raddevon/flask-permissions
#from flask_permissions.core import Permissions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_socketio import SocketIO
from app.Vendor.Code import Code
from app.env import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, UPLOAD_FOLDER, MAX_CONTENT_LENGTH

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
@app.errorhandler(Exception)
def error_handler(e):
    return ExceptionApi(Code.ERROR, e)

@socketio.on_error_default       # Handles the default namespace
def error_handler(e):
    return ExceptionApi(Code.ERROR, e)
#引入使用的控制器
from app.Controllers import  UsersController, SocketController, RestfulController, AdminController
# 蓝图，新增的后台部分代码
from app.Controllers.AdminController import admin
app.register_blueprint(admin, url_prefix='/admin')
