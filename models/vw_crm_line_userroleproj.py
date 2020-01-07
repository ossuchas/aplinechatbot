from db import db
from typing import List
from datetime import datetime


class UserRoleProjModel(db.Model):
    __tablename__ = "vw_crm_line_userroleproj"

    rec_id = db.Column(db.String(200), primary_key=True)
    projectcode = db.Column(db.String(50))
    project_name = db.Column(db.String(255))
    display_project = db.Column(db.String(255))
    bg = db.Column(db.String(5))
    subbg = db.Column(db.String(50))
    user_empcode = db.Column(db.String(50))
    user_token_Id = db.Column(db.String(255))

    @classmethod
    def find_by_emp(cls, _emp_code: str) -> List["UserRoleProjModel"]:
        return cls.query.filter_by(user_empcode=_emp_code).order_by(cls.projectcode.asc()).all()

    @classmethod
    def find_by_userid(cls, _userid: str) -> List["UserRoleProjModel"]:
        return cls.query.filter_by(user_token_Id=_userid).order_by(cls.projectcode.asc()).all()

