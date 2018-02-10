from app import app
from app.Controllers.BaseController import BaseController
from app.Models.Users import Users
from app.Vendor.UsersAuthJWT import UsersAuthJWT
from flask import request
''' 注册 '''


@app.route('/register', methods=['POST'])
def register():
    rules = {
        'email': {
            'type': 'string',
            'minlength': 10,
            'maxlength': 20
        },
        'password': {
            'type': 'string',
            'minlength': 10,
            'maxlength': 20
        }
    }
    error_msg = {
        'name': {
            'type': u'姓名必须是字符串',
            'minlength': u'姓名必须小于20',
            'maxlength': u'姓名必须大于10'
        },
        'password': {
            'type': u'密码必须是字符串',
            'minlength': u'密码必须小于20',
            'maxlength': u'密码必须大于10'
        }
    }
    error = BaseController().validateInput(rules, error_msg)
    if(error is not True):
        return error
    email = request.form.get('email')
    password = Users.set_password(request.form.get('password'))
    user = Users(
        email=email,
        password=password,
        status=1)
    user.add(user)
    if user.id:
        return BaseController().successData('注册成功')
    return BaseController().error('注册失败')


''' 登录 '''


@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if (not email or not password):
        return BaseController().successData('用户名和密码不能为空')
    else:
        result = UsersAuthJWT.authenticate(UsersAuthJWT, email, password)
        return BaseController().successData(result)


''' 获取用户信息 
jwt中修改error处理方法,统一响应头
_default_jwt_error_handler
'''


@app.route('/user', methods=['GET'])
def get():
    result = UsersAuthJWT().identify(request)
    if isinstance(result, str):
        return BaseController().error(result)
    if (result['data']):
        user = Users.get(result['data']['id'])
        returnUser = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'login_time': user.updated_at
        }
    return BaseController().successDataToMsgJson(returnUser)