from models.ICON_EntForms_Products import ICON_EntForms_ProductsModel as crm_pd


def find_crm_product_by_id(productid: str = None) -> str:

    products = crm_pd().sp_find_products()

    return products[1]
