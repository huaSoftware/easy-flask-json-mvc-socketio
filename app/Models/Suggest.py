from app import db
from app.Models.BaseModel import BaseModel
from app.Models.Users import Users
from sqlalchemy_serializer import SerializerMixin


class Suggest(BaseModel, db.Model, SerializerMixin):
    __tablename__ = 'suggest'
    id = db.Column(db.Integer, primary_key=True)
    add_time = db.Column(db.Integer)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 外键对象，不会生成数据库实际字段
    User = db.relationship('Users')
    message = db.Column(db.String(255))

    # 一对多普通方式
    @staticmethod
    def on_to_many():
        data = Suggest.query.filter(Users.id == Suggest.users_id).all()
        # all方法返回列表要进行处理才能调用sqlalchemy_serializer的to_dict方法
        data_msg = BaseModel.db_l_to_d(data)
        return data_msg

    # 一对多join方式
    @staticmethod
    def join():
        data = Suggest.query.join(Users, Users.id == Suggest.users_id).all()
        data_msg = BaseModel.db_l_to_d(data)
        return data_msg

    # 一对多left join
    @staticmethod
    def leftJoin():
        data = Suggest.query.outerjoin(Users, Users.id == Suggest.users_id).all()
        data_msg = BaseModel.db_l_to_d(data)
        return data_msg