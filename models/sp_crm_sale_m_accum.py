from db import db
from typing import List


class SaleMonthAccumModel(db.Model):
    __tablename__ = "ICON_EntForms_Transfer"

    TransferNumber = db.Column(db.String(50), primary_key=True)
    RunningNumber = db.Column(db.Integer)

    def sp_crm_sale_m_accum(self):
        sql_statement = """
           EXEC [dbo].[sp_crm_sale_m_accum] @param = 0
           """
        return db.session.execute(sql_statement).fetchone()
