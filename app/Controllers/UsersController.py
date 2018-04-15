from app import app
from app.Controllers.BaseController import BaseController
from app.Models.Users import Users
from app.Models.Suggest import Suggest
from app.Vendor.UsersAuthJWT import UsersAuthJWT
from flask import request
from werkzeug.utils import secure_filename
import os
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
            'minlength': u'姓名必须大于10',
            'maxlength': u'姓名必须小于20'
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


'''
*获取用户信息 
*jwt中修改error处理方法,统一响应头
*_default_jwt_error_handler
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


''' 查询用户留言记录，一对多
'''


@app.route('/user/suggest', methods=['GET'])
def userSuggest():
    data_msg = Suggest.on_to_many()
    return BaseController().successDataToMsgJson(data_msg)


# join


@app.route('/user/suggest/join', methods=['GET'])
def userSuggestJoin():
    data_msg = Suggest.join()
    return BaseController().successDataToMsgJson(data_msg)

# left join
# 如果想使用right join的话 把类颠倒下即可。


@app.route('/user/suggest/left', methods=['GET'])
def userSuggestLeft():
    data_msg = Suggest.leftJoin()
    return BaseController().successDataToMsgJson(data_msg)

    
""" 上传文件并验证
    https://zhuanlan.zhihu.com/p/23731819?refer=flask
"""
@app.route('/document/upload', methods=['POST'])
def documentUpload():
    files = request.files['document']
    filename = secure_filename(files.filename)
    if(files and BaseController.allowed_file(filename)):
        path = os.getcwd()+"/uploads/"+filename
        files.save(path)
        return '你成功走通了'
    #size = len(files.read())
    return '文件类型错误'

