from app import db
from app.Models.BaseModel import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from app.Vendor.Decorator import classTransaction


class Users(db.Model, BaseModel, SerializerMixin):
    __tablename__ = 'users'
    __schema_extend__ = ('-password',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255))
    tel = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(255))
    status = db.Column(db.Integer)
    remember_token = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.Integer, nullable=True)
    updated_at = db.Column(db.Integer, nullable=True)
    # 描述suggest表关系，第一个参数是参照类,要引用的表，
    # 第二个参数是backref为类Suggest申明的新方法，backref为定义反向引用，
    # 第三个参数lazy是决定什么时候sqlalchemy从数据库中加载数据
    #这里缺少外键，暂不展开
    #suggest = db.relationship('Suggest')

    """  def __str__(self):
        return "User(id='%s')" % self.id """

    #设置密码
    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    #校验密码
    @staticmethod
    def check_password(hash_password, password):
        return check_password_hash(hash_password, password)

    #获取用户信息
    @staticmethod
    def get(id):
        return Users.query.filter_by(id=id).first()

    # 增加用户
    @classTransaction
    def add(self, user):
        db.session.add(user)
        return True

    # 根据id删除用户
    def delete(self, id):
        self.query.filter_by(id=id).delete()
        return db.session.commit()

    # 更新更新时间
    @staticmethod
    def update(email, updated_at):
        Users.query.filter_by(email=email).update({'updated_at': updated_at})
        return db.session.commit()
