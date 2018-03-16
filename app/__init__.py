from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from app.env import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
import pymysql
pymysql.install_as_MySQLdb()
#普通json带error_code风格使用此app示例
app = Flask(__name__)
# 实例化websocket
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
# 配置 sqlalchemy  数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
# 初始化
db = SQLAlchemy(app)
#引入使用的控制器
from app.Controllers import MusicController, UsersController, SocketController
# 蓝图，新增的后台部分代码
from app.Controllers.AdminController import admin
app.register_blueprint(admin, url_prefix='/admin')
