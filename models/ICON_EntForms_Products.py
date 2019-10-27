from db import db
from typing import List


class ICON_EntForms_ProductsModel(db.Model):
    __tablename__ = "ICON_EntForms_Products"

    ItemID = db.Column(db.String(50), primary_key=True)
    ProductID = db.Column(db.String(15))

    def sp_find_products(self):
        sql_statement = """
           EXECUTE dbo.sp_kai_products @param1 = 0
           """
        return db.session.execute(sql_statement).fetchone()

