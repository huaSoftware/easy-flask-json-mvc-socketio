''' author:hua
    date:2018.2.6
    基础控制器，封装一些基础方法 
    验证库https://cerberus.readthedocs.io/en/stable/index.html
'''
from app.config import DEBUG_LOG
from flask import request, jsonify
import cerberus
import logging
import time
import json


class CustomErrorHandler(cerberus.errors.BasicErrorHandler):
    def __init__(self, tree=None, custom_messages=None):
        super(CustomErrorHandler, self).__init__(tree)
        self.custom_messages = custom_messages or {}

    def format_message(self, field, error):
        tmp = self.custom_messages
        for x in error.schema_path:
            try:
                tmp = tmp[x]
            except KeyError:
                return super(CustomErrorHandler, self).format_message(
                    field, error)
        if isinstance(tmp, dict):
            return super(CustomErrorHandler, self).format_message(field, error)
        else:
            return tmp


class Controller:

    ''' 
    * 验证输入信息
    * @param  array $rules
    * @return response
    '''
    def validateInput(self, rules, error_msg=''):
        v = cerberus.validator(
            rules, error_handler=CustomErrorHandler(custom_messages={error_msg}))
        requests = request.args
        if (v.validate(requests)):
            return True
        return v.errors

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

    '''
    * 返回Json数据
    * @param  array   $data
    * @param  array   $ext
    * @param  array   $paged
    * @return json
    '''
    def json(self, body=''):
        if (DEBUG_LOG):
            debug_id = self.uniqid()
            self.log().error(
                json.dumps({
                    'LOG_ID': debug_id,
                    'IP_ADDRESS': request.remote_addr,
                    'REQUEST_URL': request.url,
                    'REQUEST_METHOD': request.method,
                    'PARAMETERS': request.args,
                    'RESPONSES': body
                }))
        body['debug_id'] = debug_id
        return jsonify(body)

    def error(self, msg=''):
        return self.json({'error_code': 400, 'error': True, 'msg': msg})

    def successData(self, msg=''):
        return self.json({'error_code': 200, 'msg': msg})

    def uniqid(self, prefix=''):
        return prefix + hex(int(time.time()))[2:10] + hex(int(time.time() * 1000000) % 0x100000)[2:7]
