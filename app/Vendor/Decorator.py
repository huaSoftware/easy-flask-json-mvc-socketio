from app import db
from flask import request
from functools import wraps
from app.Controllers.BaseController import BaseController

""" 
    事务装饰器,不能用于类方法
    @params func
    @return func|False
"""
def transaction(func):
    @wraps(func)
    def inner_wrappar(*args, **kwargs):
        try:
            #print('something before')
            result = func(*args, **kwargs)
            db.session.commit()
            #print('something after')
            return result
        except  Exception as e:
            print(e)
            db.session.rollback()  
            return False
    return inner_wrappar 

""" 
    事务装饰器,用于类方法
    @params func
    @return func|False
"""
def classTransaction(func):
    @wraps(func)
    def wrappar(self, *args, **kwargs):
        try:
            #print('something before')
            result = func(self, *args, **kwargs)
            db.session.commit()
            #print('something after')
            return result
        except  Exception as e:
            print(e)
            db.session.rollback()  
            return False
    return wrappar 

""" 
    验证装饰器 
    @params name 字段名
    @params rules 规则
    @params msg 描述
    @return func|json
"""
def validator(name, rules, msg):
    # 装饰器就是把其他函数作为参数的函数
    def wrappar(func):
        @wraps(func)
        def inner_wrappar(*args, **kwargs):
            #print('%s: something before'%name)
            error = BaseController().validateInputByName(name, {name: rules}, {name:msg})
            if(isinstance(error, dict) == False):
                return error
            return func(error)
        return inner_wrappar 
    return wrappar
