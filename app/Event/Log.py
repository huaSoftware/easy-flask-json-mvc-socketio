'''
@Author: hua
@Date: 2019-12-03 14:13:15
@description: 
@LastEditors: hua
@LastEditTime: 2019-12-03 14:51:34
'''
from app.Models.Log import Log
from sqlalchemy import event
import time

@event.listens_for(Log, "before_insert")
def log_before_insert(mapper, connection, target):
    target.create_time = int(time.time())