'''
@Author: hua
@Date: 2018-08-30 10:52:23
@description: 
@LastEditors: hua
@LastEditTime: 2019-07-08 08:59:32
'''
from app import dBSession
from app.Models.BaseModel import BaseModel
from sqlalchemy_serializer import SerializerMixin
from app.Vendor.Utils import Utils
from app.Models.Model import HtComment


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
        
    @staticmethod
    def getCommentsList(page, per_page):
        dataObj = dBSession.query(Comments).order_by(Comments.add_time.desc()).paginate(
            page, per_page=per_page, error_out=False)
        paginate = BaseModel.formatPaged(page, per_page, dataObj.total)
        commentsList = Utils.db_l_to_d(dataObj.items)
        data = BaseModel.formatBody(
            {"paged": paginate, "commentsList": commentsList})
        return data
