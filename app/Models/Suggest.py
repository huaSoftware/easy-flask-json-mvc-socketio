from app import db
from app.Models.BaseModel import BaseModel
from app.Models.Users import Users
from sqlalchemy_serializer import SerializerMixin
from app.Vendor.Utils import Utils


class Suggest(BaseModel, db.Model, SerializerMixin):
    __tablename__ = 'suggest'
    id = db.Column(db.Integer, primary_key=True)
    add_time = db.Column(db.Integer)
    #外键申明
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #user表虚拟对象，关联的内容会在user对象中
    # 第二个参数是backref会添加一个对象给suggest模型，容易造成递归堆栈超出，超级不建议使用！
    # 第三个参数lazy是决定什么时候sqlalchemy从数据库中加载数据
    #uselist=False一对一关系，true是一对多
    # , backref = 'users'
    users = db.relationship('Users')  # backref='suggest'这个是毒瘤，不用！！！
    message = db.Column(db.String(255))
    
    # 一对多普通方式
    @staticmethod
    def on_to_many():
        data = Suggest.query.filter(Users.id == Suggest.users_id).all()
        # all方法返回列表要进行处理才能调用sqlalchemy_serializer的to_dict方法
        data_msg = Utils.db_l_to_d(data)
        return data_msg

    # 一对多join方式
    @staticmethod
    def join():
        data = Suggest.query.join(Users, Users.id == Suggest.users_id).all()
        data_msg = Utils.db_l_to_d(data)
        return data_msg

    # 一对多left join
    @staticmethod
    def leftJoin():
        data = Suggest.query.outerjoin(Users, Users.id == Suggest.users_id).all()
        data_msg = Utils.db_l_to_d(data)
        return data_msg
