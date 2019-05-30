'''
@Author: hua
@Date: 2019-05-30 10:41:29
@LastEditors: hua
@LastEditTime: 2019-05-30 13:42:07
'''
from flask import jsonify, make_response
from app.Vendor.Log import log
from app.Vendor.Utils import Utils
import traceback

def ExceptionApi(code, e):
    """ 接口异常处理 """
    log().exception(e)
    body = {}
    body['error_code'] = code
    body['error'] = True
    body['show'] = False
    body['debug_id'] = Utils.unique_id()
    body['traceback'] = traceback.format_exc()
    return make_response(jsonify(body))