'''
@Author: hua
@Date: 2018-08-30 10:52:23
@description: 
@LastEditors: hua
@LastEditTime: 2019-07-08 08:59:29
'''
from app import dBSession
from app.Models.BaseModel import BaseModel
from sqlalchemy_serializer import SerializerMixin
from app.Vendor.Utils import Utils
from app.Models.Model import HtImgShard

class ImgShard(HtImgShard, BaseModel, SerializerMixin):
  
    # 增加分片数据
    @staticmethod
    def add(index, uuid, imgString):
        data = ImgShard(index=index, uuid=uuid, imgString=imgString)
        dBSession.add(data)
        return dBSession.commit()

    #根据uuid获取分片数据
    @staticmethod
    def getData(uuid):
        obj = dBSession.query(ImgShard).filter_by(uuid = uuid).order_by('index').all()
        data = Utils.db_l_to_d(obj)
        return data
