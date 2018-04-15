#mysql
SQLALCHEMY_DATABASE_URI = 'mysql://root:1993524@localhost:3306/text?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
#debug
DEBUG_LOG = True
#upload
UPLOAD_FOLDER = '/uploads/'# 允许目录
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 允许大小16MB
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])  # 允许文件
#jwt
SECRET_KEY = '7PXsHcHGfa4e3kEs8Rvcv8ymjI0UeauX'
JWT_LEEWAY = 604800
