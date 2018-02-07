''' author:hua
    date:2018.2.6
    基础模型，封装一些基础方法 
'''
from app import app
from app import db
from flask import request, jsonify, abort
import time


class BaseModel():
    SUCCESS = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404

    def formatPaged(page, size, total):
        if int(total) > int(page) * int(size):
            more = 1
        else:
            more = 0
        return {
            'total': int(total),
            'page': int(page),
            'size': int(size),
            'more': more
        }

    def formatBody(data={}):
        data['error_code'] = 200
        return data

    def formatError(code, message=''):
        if code == BAD_REQUEST:
            message = 'Bad request.'
        elif code == NOT_FOUND:
            message = 'No result matched.'
        body = {}
        body['error'] = True
        body['error_code'] = code
        body['msg'] = message
        return body

    def log(self):
        logger = logging.getLogger("error_msg")
        logger.setLevel(logging.DEBUG)
        # 建立一个filehandler来把日志记录在文件里，级别为debug以上
        fh = logging.FileHandler("spam.log")
        fh.setLevel(logging.DEBUG)
        # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # 设置日志格式
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # 将相应的handler添加在logger对象中
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger
