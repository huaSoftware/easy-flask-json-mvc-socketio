from app import db
from app.Models.BaseModel import BaseModel
from sqlalchemy_serializer import SerializerMixin
from app.Vendor.Utils import Utils


class ImgShard(db.Model, BaseModel, SerializerMixin):
    __tablename__ = 'imgShard'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(100))
    imgString = db.Column(db.String(5500))
    index = db.Column(db.Integer)
  
    # 增加分片数据
    @staticmethod
    def add(index, uuid, imgString):
        data = ImgShard(index=index, uuid=uuid, imgString=imgString)
        db.session.add(data)
        return db.session.commit()

    #根据uuid获取分片数据
    @staticmethod
    def getData(uuid):
        obj = ImgShard.query.filter_by(uuid = uuid).order_by('index').all()
        data = Utils.db_l_to_d(obj)
        return data
