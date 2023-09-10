from Models.order_details import Details
from Models.products import Products
from Models.db2 import session
from sqlalchemy import func, desc
import json

#Producto más vendido
def report_product():
    details = session.query(Details.id_product, func.sum(Details.quantity).label("quantity")).group_by(Details.id_product).order_by(desc("quantity")).first()
    id_product = details[0]
    product = session.query(Products).get(id_product)
    response = {"Resultado":f"El producto mas vendido es el {product.name}"}
    response = {"statusCode": 200, "body": json.dumps(response)}
    return response