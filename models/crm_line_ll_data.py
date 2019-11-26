from db import db
from typing import List


class LeadLagModel(db.Model):
    __tablename__ = "crm_line_ll_data"

    ll_id = db.Column(db.Integer, primary_key=True)
    bg = db.Column(db.String(255))
    years = db.Column(db.Float)
    quarter = db.Column(db.Float)
    week = db.Column(db.String(255))
    period = db.Column(db.String(255))
    tg_transferamount = db.Column(db.Float)
    at_transferamount = db.Column(db.Float)
    icon_transferamount = db.Column(db.String(255))
    tg_transferunit = db.Column(db.Float)
    at_transferunit = db.Column(db.Float)
    icon_transferunit = db.Column(db.String(255))
    tg_qcpass = db.Column(db.Float)
    at_qcpass = db.Column(db.Float)
    icon_qcpass = db.Column(db.String(255))
    tg_checkunit = db.Column(db.Float)
    at_checkunit = db.Column(db.Float)
    icon_checkunit = db.Column(db.String(255))
    tg_acceptunit = db.Column(db.Float)
    at_acceptunit = db.Column(db.Float)
    icon_acceptunit = db.Column(db.String(255))
    tg_bankapprove = db.Column(db.Float)
    at_bankapprove = db.Column(db.Float)
    icon_bankapprove = db.Column(db.String(255))
    tg_grosspresalesamount = db.Column(db.Float)
    at_grosspresalesamount = db.Column(db.Float)
    icon_grosspresalesamount = db.Column(db.String(255))
    tg_netpresalesamount = db.Column(db.Float)
    at_netpresalesamount = db.Column(db.Float)
    icon_netpresalesamount = db.Column(db.String(255))
    tg_netpresales_precancelamount = db.Column(db.Float)
    at_netpresales_precancelamount = db.Column(db.Float)
    icon_netpresales_precancelamount = db.Column(db.String(255))
    tg_precancelamount = db.Column(db.Float)
    at_precancelamount = db.Column(db.Float)
    icon_precancelamount = db.Column(db.String(255))
    tg_grosspresalesunit = db.Column(db.Float)
    at_grosspresalesunit = db.Column(db.Float)
    icon_grosspresalesunit = db.Column(db.String(255))
    tg_netpresalesunit = db.Column(db.Float)
    at_netpresalesunit = db.Column(db.Float)
    icon_netpresalesunit = db.Column(db.String(255))
    tg_netpresales_precancelunit = db.Column(db.Float)
    at_netpresales_precancelunit = db.Column(db.Float)
    icon_netpresales_precancelunit = db.Column(db.String(255))
    tg_precancelunit = db.Column(db.Float)
    at_precancelunit = db.Column(db.Float)
    icon_precancelunit = db.Column(db.String(255))
    tg_walk = db.Column(db.Float)
    at_walk = db.Column(db.Float)
    icon_walk = db.Column(db.String(255))
    tg_walk2 = db.Column(db.Float)
    at_walk2 = db.Column(db.Float)
    icon_walk2 = db.Column(db.String(255))
    tg_conversion = db.Column(db.Float)
    at_conversion = db.Column(db.Float)
    icon_conversion = db.Column(db.String(255))

    @classmethod
    def find_by_week(cls) -> "LeadLagModel":
        return cls.query.filter_by(period='W').first()

    @classmethod
    def find_by_qtd(cls) -> "LeadLagModel":
        return cls.query.filter_by(period='QTD').first()

    @classmethod
    def find_by_ytd(cls) -> "LeadLagModel":
        return cls.query.filter_by(period='YTD').first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
