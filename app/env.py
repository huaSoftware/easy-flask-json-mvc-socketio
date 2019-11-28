'''
@Author: hua
@Date: 2018-08-30 10:52:23
@description: 
@LastEditors: hua
@LastEditTime: 2019-11-28 20:05:49
'''
#mysql
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1993524@localhost:3306/test?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
#debug
DEBUG_LOG = True
#log save 1为文件形式，2为数据库形式，默认数据库
SAVE_LOG = 1
#upload
UPLOAD_FOLDER = '/uploads/'# 允许目录
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 允许大小16MB
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])  # 允许文件
#jwt
SECRET_KEY = '7PXsHcHGfa4e3kEs8Rvcv8ymjI0UeauX'
JWT_LEEWAY = 604800
