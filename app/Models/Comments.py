'''
@Author: hua
@Date: 2018-08-30 10:52:23
@description: 
@LastEditors: hua
@LastEditTime: 2019-07-10 09:31:05
'''
from app import dBSession
from app.Models.BaseModel import BaseModel
from sqlalchemy_serializer import SerializerMixin
from app.Vendor.Utils import Utils
from app.Models.Model import HtComment
import math

class Comments(HtComment, BaseModel, SerializerMixin):
    serialize_rules = ('update_time', '-add_time')
    #不建议用setattr，会影响父类
    """  def __setattr__(self, *args, **kwargs):
        args[1].class_.add_time = 1
        print('call func set attr')
        return object.__setattr__(self, *args, **kwargs) """
    #扩展自定义字段,配合schema_extend可以重新自定义数据表字段名及值
    @property
    def update_time(self):
        update = self.add_time
        return update
        
    def getCommentsList(self, page, per_page):

        data = self.getList({}, Comments.add_time.desc(),(), page, per_page)
        
        return data
    
    """ 
        列表
        @param set filters 查询条件
        @param obj order 排序
        @param tuple field 字段
        @param int offset 偏移量
        @param int limit 取多少条
        @return dict
    """
    def getList(self, filters, order, field=(), offset = 0, limit = 15):
        res = {}
        res['page'] ={}
        res['page']['count'] = dBSession.query(Comments).filter(*filters).count()
        res['list'] = []
        res['page']['total_page'] = self.get_page_number(res['page']['count'], limit)
        res['page']['current_page'] = offset
        if offset != 0:
            offset = (offset - 1) * limit

        if res['page']['count'] > 0:
            res['list'] = dBSession.query(UserRoomRelation).filter(*filters)
            res['list'] = res['list'].order_by(order).offset(offset).limit(limit).all()
        if not field:
            res['list'] = [c.to_dict() for c in res['list']]
        else:
            res['list'] = [c.to_dict(only=field) for c in res['list']]
        return res

    @staticmethod
    def get_page_number(count, page_size):
        count = float(count)
        page_size = abs(page_size)
        if page_size != 0:
            total_page = math.ceil(count / page_size)
        else:
            total_page = math.ceil(count / 5)
        return total_page