from db import db
from typing import List
from datetime import datetime


class LogChatBotModel(db.Model):
    __tablename__ = "log_linechatbot"

    logid = db.Column(db.Integer, primary_key=True)
    replyToken = db.Column(db.String(255))
    source_userId = db.Column(db.String(255))
    source_type = db.Column(db.String(50))
    timestamps = db.Column(db.String(100))
    message_type = db.Column(db.String(50))
    message_text = db.Column(db.String(4000))
    stickerId = db.Column(db.String(10))
    packageId = db.Column(db.String(5))

    @classmethod
    def find_by_id(cls, _logid: int) -> "LogChatBotModel":
        return cls.query.filter_by(logid=_logid).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()