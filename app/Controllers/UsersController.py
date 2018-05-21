from app import app
from app.Controllers.BaseController import BaseController
from app.Vendor.Utils import Utils
from app.Models.Users import Users
from app.Models.Suggest import Suggest
from app.Models.Comments import Comments
from app.Vendor.UsersAuthJWT import UsersAuthJWT
from flask import request
from werkzeug.utils import secure_filename
import os
import base64

''' 注册 '''


@app.route('/api/v2/register', methods=['POST'])
def register():
    rules = {
        'email': {
            'required': True,
            'type': 'string',
            'minlength': 10,
            'maxlength': 20
        },
        'password': {
            'required': True,
            'type': 'string',
            'minlength': 6,
            'maxlength': 20
        }
    }
    error_msg = {
        'email': {
            'required': u'邮箱是必须的',
            'type': u'邮箱必须是字符串',
            'minlength': u'邮箱必须大于10',
            'maxlength': u'邮箱必须小于20'
        },
        'password': {
            'required': u'密码是必须的',
            'type': u'密码必须是字符串',
            'minlength': u'密码必须大于6',
            'maxlength': u'密码必须小于20'
        }
    }
    error = BaseController().validateInput(rules, error_msg)
    if(error is not True):
        return error
    email = request.json.get('email')
    password = Users.set_password(request.json.get('password'))
    
    userData = Users.query.filter_by(email=email).first()
    if(userData == None):
        user = Users(
            email=email,
            password=password,
            status=1)
        user.add(user)
        if user.id:
            return BaseController().successData(msg='注册成功')
        return BaseController().error('注册失败')
    return BaseController().error('账号已注册')


''' 登录 '''


@app.route('/api/v2/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if (not email or not password):
        return BaseController().error('用户名和密码不能为空')
    else:
        result = UsersAuthJWT.authenticate(email, password)
        return result


'''
*获取用户信息 
*jwt中修改error处理方法,统一响应头
*_default_jwt_error_handler
'''


@app.route('/api/v2/user', methods=['GET'])
def get():
    #鉴权
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
    return BaseController().successData(returnUser)


""" 不通过鉴权获取用户信息 """


@app.route('/api/v2/userInfo', methods=['POST'])
def getInfo():
    id = request.json.get('id')
    data = Users.query.filter_by(id=id).all()
    datas = Utils.db_l_to_d(data)
    return BaseController().successData(datas)


''' 查询用户留言记录，一对多
'''


@app.route('/api/v2/user/suggest', methods=['GET'])
def userSuggest():
    data_msg = Suggest.on_to_many()
    return BaseController().successData(data_msg)


# join


@app.route('/api/v2/user/suggest/join', methods=['GET'])
def userSuggestJoin():
    data_msg = Suggest.join()
    return BaseController().successData(data_msg)

# left join
# 如果想使用right join的话 把类颠倒下即可。


@app.route('/api/v2/user/suggest/left', methods=['GET'])
def userSuggestLeft():
    data_msg = Suggest.leftJoin()
    return BaseController().successData(data_msg)

    
""" 上传文件并验证
    https://zhuanlan.zhihu.com/p/23731819?refer=flask
"""


@app.route('/api/v2/document/upload', methods=['POST'])
def documentUpload():
    files = request.files['document']
    filename = secure_filename(files.filename)
    if(files and Utils.allowed_file(filename)):
        path = os.getcwd()+"/uploads/"+filename
        files.save(path)
        return BaseController().error('你成功走通了')
    return BaseController().error('文件类型错误')


"""上传base64形式文件并杨峥
    需要前端传入文件类型
"""


@app.route('/api/v2//document/upload/base64', methods=['post'])
def documentUploadBase64():
    #二维数组验证
    rules = {
        'userImgOne': { 
            'type': 'dict',
            'schema': {
                'imgBase64':{
                    'required': True,
                    'type': 'string',
                    'minlength': 2
                },
                'name': {
                    'required': True,
                    'type': 'string',
                    'minlength': 2
                },
                'size': {
                    'required': True,
                    'type': 'integer',
                    'minlength': 2
                },
                'type': {
                    'required': True,
                    'type': 'string',
                    'minlength': 2
                }
            }
         },
        'userImgTwo': {
            'type': 'dict',
            'schema': {
                'imgBase64': {
                    'required': True,
                    'type': 'string',
                    'minlength': 2
                },
                'name': {
                    'required': True,
                    'type': 'string',
                    'minlength': 2
                },
                'size': {
                    'required': True,
                    'type': 'integer',
                    'minlength': 2
                },
                'type': {
                    'required': True,
                    'type': 'string',
                    'minlength': 2
                }
            }
        },
        'userImgThree': {
            'type': 'dict',
            'schema': {
                'imgBase64': {
                    'required': True,
                    'type': 'string',
                    'minlength': 2
                },
                'name': {
                    'required': True,
                    'type': 'string',
                    'minlength': 2
                },
                'size': {
                    'required': True,
                    'type': 'integer',
                    'minlength': 2
                },
                'type': {
                    'required': True,
                    'type': 'string',
                    'minlength': 2
                }
            }   
        }
    }
    error_msg = {
        'userImgOne': {
            'type': 'dict',
            'schema': {
                'imgBase64':{
                'required': u'图一是必须的',
                'type': u'图一必须是字符串',
                'minlength': u'图一字符最小是2'
                },
                'name': {
                    'required': u'图一是必须的',
                    'type':  u'图一必须是字符串',
                    'minlength': u'图一字符最小是2'
                },
                'size': {
                    'required': u'图一是必须的',
                    'type': u'图一必须是字符串',
                    'minlength': u'图一字符最小是2'
                },
                'type': {
                    'required': u'图一是必须的',
                    'type': u'图一必须是字符串',
                    'minlength': u'图一字符最小是2'
                }
            }
        },
        'userImgTwo': {
            'type': 'dict',
            'schema': {
                'imgBase64': {
                    'required': u'图二是必须的',
                    'type': u'图二必须是字符串',
                    'minlength': u'图二字符最小是2'
                },
                'name': {
                    'required': u'图二是必须的',
                    'type':  u'图二必须是字符串',
                    'minlength': u'图二字符最小是2'
                },
                'size': {
                    'required': u'图二是必须的',
                    'type': u'图二必须是整数',
                    'minlength': u'图二字符最小是2'
                },
                'type': {
                    'required': u'图二是必须的',
                    'type': u'图二必须是字符串',
                    'minlength': u'图二字符最小是2'
                }
            }
        },
        'userImgThree': {
            'type': 'dict',
            'schema': {
                'imgBase64':{
                    'required': u'图三是必须的',
                    'type': u'图三必须是字符串',
                    'minlength': u'图三字符最小是2'
                },
                'name': {
                    'required': u'图三是必须的',
                    'type':  u'图三必须是字符串',
                    'minlength': u'图三字符最小是2'
                },
                'size': {
                    'required': u'图三是必须的',
                    'type': u'图三必须是整数',
                    'minlength': u'图三字符最小是2'
                },
                'type': {
                    'required': u'图三是必须的',
                    'type': u'图三必须是字符串',
                    'minlength': u'图三字符最小是2'
                }
            }
        }
    }
    error = BaseController().validateInput(rules, error_msg)
    if(error is not True):
        return error
    #这边图片类型，大小判断请根据需求自己判断，暂不展开
    for(k,v) in request.json.items():
       userImg = v['imgBase64'].split(',')[1]
       imgdata = base64.b64decode(userImg)
       path = os.getcwd()+"/uploads/"+Utils.uniqid()+'.jpg'
       file = open(path, 'wb')
       file.write(imgdata)
       file.close()
    """userImgOne = request.json.get('userImgOne')['imgBase64'].split(',')[1]
    userImgTwo = request.json.get('userImgTwo')['imgBase64'].split(',')[1]
    userImgThree = request.json.get('userImgThree')['imgBase64'].split(',')[1]
    imgdata = base64.b64decode(userImgOne) """
    return BaseController().successData(msg='图片提交成功')


@app.route('/api/v2/comments/get', methods=['post'])
def commentsGet():
    rules = {
        'pageNo': {
            'required': True,
            'type': 'integer'
        },
        'pageSize': {
            'required': True,
            'type': 'integer'
        }
    }
    error_msg = {
        'pageNo': {
            'required': u'当前页是必须的',
            'type': u'当前页必须是整数'
        },
        'pageSize': {
            'required': u'当前页是必须的',
            'type': u'当前页必须是整数'
        }
    }
    error = BaseController().validateInput(rules, error_msg)
    if(error is not True):
        return error
    pageNo = request.json.get('pageNo')
    pageSize = request.json.get('pageSize')
    data =Comments.getCommentsList(pageNo, pageSize)
    return BaseController().json(data)
