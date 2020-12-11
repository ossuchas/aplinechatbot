from db import db
from typing import List
from datetime import datetime


class MstMsgConfigModel(db.Model):
    __tablename__ = "chatbot_mst_conf"

    user_id = db.Column(db.Integer, primary_key=True)
    msg_json = db.Column(db.String(8000))
    modifyby = db.Column(db.String(20))
    modifydate = db.Column(db.DateTime)

    @classmethod
    def find_by_id(cls, _user_id: int) -> "MstMsgConfigModel":
        return cls.query.filter_by(user_id=_user_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
