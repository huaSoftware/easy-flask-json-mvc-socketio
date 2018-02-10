from app import db
from app.Models.BaseModel import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin


class Users(db.Model, BaseModel, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255))
    tel = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(255))
    status = db.Column(db.Integer)
    remember_token = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.Integer, nullable=True)
    updated_at = db.Column(db.Integer, nullable=True)
    img_path = db.Column(db.String(100), nullable=True)

    def __str__(self):
        return "User(id='%s')" % self.id

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    @staticmethod
    def check_password(hash_password, password):
        return check_password_hash(hash_password, password)

    @staticmethod
    def get(id):
        return Users.query.filter_by(id=id).first()

    def add(self, user):
        db.session.add(user)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, id):
        self.query.filter_by(id=id).delete()
        return db.session.commit()