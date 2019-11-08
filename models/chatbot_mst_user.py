from db import db
from typing import List
from datetime import datetime


class MstUserModel(db.Model):
    __tablename__ = "chatbot_mst_user"

    user_id = db.Column(db.Integer, primary_key=True)
    user_token_Id = db.Column(db.String(255))
    user_name = db.Column(db.String(255))
    user_full_name = db.Column(db.String(255))
    createby = db.Column(db.String(20))
    createdate = db.Column(db.DateTime)
    modifyby = db.Column(db.String(20))
    modifydate = db.Column(db.DateTime)

    @classmethod
    def find_by_id(cls, _user_id: int) -> "MstUserModel":
        return cls.query.filter_by(user_id=_user_id).first()

    @classmethod
    def find_by_token_id(cls, _user_token_id: int) -> "MstUserModel":
        return cls.query.filter_by(user_token_Id=_user_token_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
