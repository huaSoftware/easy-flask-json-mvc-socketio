from app.Models.Users import Users
from app.env import SECRET_KEY, JWT_LEEWAY
import datetime
import jwt
import time
''' login登录验证在此做 '''


class UsersAuthJWT():
    @staticmethod
    def encode_auth_token(user_id, updated_at):
        """
        生成认证Token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp':
                datetime.datetime.utcnow() +
                datetime.timedelta(seconds=JWT_LEEWAY),
                'iat':
                datetime.datetime.utcnow(),
                'iss':
                'ken',
                'data': {
                    'id': user_id,
                    'updated_at': updated_at
                }
            }
            return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            # payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
            # 取消过期时间验证
            payload = jwt.decode(auth_token, SECRET_KEY)
            if ('data' in payload and 'id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    def authenticate(self, email, password):
        """
        用户登录，登录成功返回token，写将登录时间写入数据库；登录失败返回失败原因
        :param password:
        :return: json
        """
        userInfo = Users.query.filter_by(email=email).first()
        if(userInfo is None):
            return '找不到用户'
        else:
            if (Users.check_password(userInfo.password, password)):
                updated_at = int(time.time())
                userInfo.updated_at = updated_at
                Users.update(email, password)
                token = self.encode_auth_token(userInfo.id, updated_at)
                return token.decode()
            else:
                return '密码不正确'

    def identify(self, request):
        """
        用户鉴权
        :return: list
        """
        auth_header = request.headers.get('Authorization')
        if (auth_header):
            auth_tokenArr = auth_header.split(" ")
            if (not auth_tokenArr or auth_tokenArr[0] != 'JWT'
                    or len(auth_tokenArr) != 2):
                return '请传递正确的验证头信息'
            else:
                auth_token = auth_tokenArr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    user = Users.get(payload['data']['id'])
                    if (user is None):
                        return '找不到该用户信息'
                    else:
                        if (user.updated_at == payload['data']['updated_at']):
                            result = payload
                        else:
                            return 'Token已更改，请重新登录获取'
                else:
                    result = payload
        else:
            return '没有提供认证token'
        return result
