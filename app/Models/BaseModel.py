'''
@Author: hua
@Date: 2018-08-30 10:52:23
@description: 
@LastEditors: hua
@LastEditTime: 2018-08-30 10:52:23
'''
''' author:hua
    date:2018.2.6
    基础模型，封装一些基础方法 
'''
import logging
from app.Vendor.Code import Code

class BaseModel():

    """ 
    * 格式化分页
    * @param int page
    * @param int size
    * @param int total
    * @return dict 
    """
    @staticmethod
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

    """ 
    * 格式化返回体
    * @param dict data
    * @return dict
    """
    @staticmethod
    def formatBody(data={}, msg='', show=True):
        dataformat = {}
        dataformat['error_code'] = Code.SUCCESS
        dataformat['data'] = data
        dataformat['msg'] = msg
        dataformat['show'] = show
        return dataformat

    """ 
    * 格式化错误返回体
    * @param int code
    * @param string message
    * @return dict
    """
    @staticmethod
    def formatError(code, message='', show=True):
        if code == Code.BAD_REQUEST:
            message = 'Bad request.'
        elif code == Code.NOT_FOUND:
            message = 'No result matched.'
        body = {}
        body['error'] = True
        body['error_code'] = Code.BAD_REQUEST
        body['msg'] = message
        body['show'] = show
        return body




