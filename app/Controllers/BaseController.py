''' author:hua
    date:2018.2.6
    基础控制器，封装一些基础方法 
    验证库https://cerberus.readthedocs.io/en/stable/index.html
'''
from app.env import DEBUG_LOG, MAX_CONTENT_LENGTH, ALLOWED_EXTENSIONS
from app.Vendor.CustomErrorHandler import CustomErrorHandlers
from flask import request, jsonify
import cerberus
import logging
import time
import json


class BaseController:

    ''' 
    * 验证输入信息
    * @param  dict rules
    * @param  string error_msg
    * @return response
    '''

    def validateInput(self, rules, error_msg=None):
        v = cerberus.Validator(
            rules, error_handler=CustomErrorHandlers(custom_messages=error_msg))
        #v = ObjectValidator(rules)
        #这边修改成json格式接收参数
        requests = request.get_json()
        if (v.validate(requests)):  # validate
            return True
        error = {}
        error['msg'] = v.errors
        error['error_code'] = 400
        error['error'] = True
        return self.json(error)

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
    * @param  dict body
    * @return json
    '''
    def json(self, body={}):
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

    '''
    * 返回错误信息
    * @param  msg string
    * @return json
    '''
    def error(self, msg=''):
        return self.json({'error_code': 400, 'error': True, 'msg': msg})

    '''
    * 返回成功信息
    * @param  msg string
    * @return json
    '''
    def successData(self, data='', msg=''):
        return self.json({'error_code': 200, 'data': data,'msg': msg})

    def successDataToMsgJson(self, data={}):
        data['error_code'] = 200
        return self.json(data)

    def uniqid(self, prefix=''):
        return prefix + hex(int(time.time()))[2:10] + hex(int(time.time() * 1000000) % 0x100000)[2:7]

