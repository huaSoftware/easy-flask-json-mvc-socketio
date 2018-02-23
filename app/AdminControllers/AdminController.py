''' 
*蓝图-后台
*引入后不用考虑Contorller方法重名等问题
'''
from flask import Blueprint
admin = Blueprint('admin', __name__)


@admin.route('/register')
def register():
    return '1'
