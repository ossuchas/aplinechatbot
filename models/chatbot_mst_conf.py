from db import db
from typing import List
from datetime import datetime


class MstMsgConfigModel(db.Model):
    __tablename__ = "chatbot_mst_conf"

    user_id = db.Column(db.Integer, primary_key=True)
    msg_type = db.Column(db.String(100))
    msg_menu = db.Column(db.String(255))
    msg_level = db.Column(db.Integer)
    msg_sub_level = db.Column(db.Integer)
    msg_value = db.Column(db.String(8000))
    msg_json = db.Column(db.String(8000))
    modifyby = db.Column(db.String(20))
    modifydate = db.Column(db.DateTime)

    @classmethod
    def find_by_id(cls, _user_id: int) -> "MstMsgConfigModel":
        return cls.query.filter_by(user_id=_user_id).first()

    @classmethod
    def find_by_msg_value(cls, _msg_value: str) -> "MstMsgConfigModel":
        return cls.query.filter_by(msg_value=_msg_value).first()

    @classmethod
    def find_by_msg_value_ds(cls, _msg_value: str, _user_type: str) -> "MstMsgConfigModel":
        return cls.query.filter_by(msg_value=_msg_value, msg_type=_user_type).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
