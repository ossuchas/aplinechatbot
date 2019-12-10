from db import db
from typing import List


class MstProjectModel(db.Model):
    __tablename__ = "vw_chatbot_mst_project"

    productid = db.Column(db.String(15), primary_key=True)
    projectname = db.Column(db.String(255))

    @classmethod
    def find_all(cls) -> List["MstProjectModel"]:
        return cls.query.filter_by().order_by(cls.projectname.asc()).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
