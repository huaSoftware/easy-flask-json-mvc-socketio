from app import db
from app.Models.BaseModel import BaseModel
from sqlalchemy_serializer import SerializerMixin
from app.Vendor.Utils import Utils


class Comments(db.Model, BaseModel, SerializerMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(100))
    user_id = db.Column(db.Integer, nullable=True)
    article_id = db.Column(db.Integer)
    add_time = db.Column(db.Integer)
   
    @staticmethod
    def getCommentsList(page, per_page):
        dataObj =  Comments.query.order_by(Comments.add_time.desc()).paginate(
            page, per_page=per_page, error_out=False)
        paginate = BaseModel.formatPaged(page, per_page, dataObj.total)
        commentsList = Utils.db_l_to_d(dataObj.items)
        data = BaseModel.formatBody(
            {"paged": paginate,"commentsList": commentsList})
        return data

