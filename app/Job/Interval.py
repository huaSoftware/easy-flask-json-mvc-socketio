'''
@Author: hua
@Date: 2019-12-12 13:42:24
@description: https://www.cnblogs.com/luxiaojun/p/6567132.html
@LastEditors: hua
@LastEditTime: 2019-12-12 13:55:52
'''
from app import sched
import time
#循环执行
@sched.scheduled_job('interval', seconds=5)
def interval_job():
    print("<interval_job>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))