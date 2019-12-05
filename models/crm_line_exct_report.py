from db import db
from typing import List
from datetime import datetime


class ExecutiveReportModel(db.Model):
    __tablename__ = "crm_line_exct_report"

    trans_id = db.Column(db.Integer, primary_key=True)
    text_msg_header = db.Column(db.String(255))
    text_msg_detail = db.Column(db.String(255))
    bg1_grosspresalesunit = db.Column(db.Float)
    bg1_grosspresalesamount = db.Column(db.Float)
    bg2_grosspresalesunit = db.Column(db.Float)
    bg2_grosspresalesamount = db.Column(db.Float)
    bg3_grosspresalesunit = db.Column(db.Float)
    bg3_grosspresalesamount = db.Column(db.Float)
    bg4_grosspresalesunit = db.Column(db.Float)
    bg4_grosspresalesamount = db.Column(db.Float)
    total_grosspresalesunit = db.Column(db.Float)
    total_grosspresalesamount = db.Column(db.Float)
    bg1_cancelunit = db.Column(db.Float)
    bg1_cancelamount = db.Column(db.Float)
    bg2_cancelunit = db.Column(db.Float)
    bg2_cancelamount = db.Column(db.Float)
    bg3_cancelunit = db.Column(db.Float)
    bg3_cancelamount = db.Column(db.Float)
    bg4_cancelunit = db.Column(db.Float)
    bg4_cancelamount = db.Column(db.Float)
    total_cancelunit = db.Column(db.Float)
    total_cancelamount = db.Column(db.Float)
    bg1_netpresalesunit = db.Column(db.Float)
    bg1_netpresalesamount = db.Column(db.Float)
    bg2_netpresalesunit = db.Column(db.Float)
    bg2_netpresalesamount = db.Column(db.Float)
    bg3_netpresalesunit = db.Column(db.Float)
    bg3_netpresalesamount = db.Column(db.Float)
    bg4_netpresalesunit = db.Column(db.Float)
    bg4_netpresalesamount = db.Column(db.Float)
    total_netpresalesunit = db.Column(db.Float)
    total_netpresalesamount = db.Column(db.Float)
    bg1_transferunit = db.Column(db.Float)
    bg1_transferamount = db.Column(db.Float)
    bg2_transferunit = db.Column(db.Float)
    bg2_transferamount = db.Column(db.Float)
    bg3_transferunit = db.Column(db.Float)
    bg3_transferamount = db.Column(db.Float)
    bg4_transferunit = db.Column(db.Float)
    bg4_transferamount = db.Column(db.Float)
    total_transferunit = db.Column(db.Float)
    total_transferamount = db.Column(db.Float)

    @classmethod
    def find_by_id(cls) -> "ExecutiveReportModel":
        return cls.query.filter_by(trans_id=1).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
