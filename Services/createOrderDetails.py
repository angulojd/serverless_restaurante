import json
from Models.db2 import session
from Models.order_details import Details
from Models.products import Products
from Models.validations import val_number

def save_details(details, id_orden, order):
    for i in details:
        id_product = val_number(i.get("id_product"), "id_product")
        if id_product[1] is False:
            response = {"statusCode": 400, "body": json.dumps(id_product[0])}
            session.delete(order)
            session.commit()
            return response
        quantity = val_number(i.get("quantity"), "quantity")
        if quantity[1] is False:
            response = {"statusCode": 400, "body": json.dumps(quantity[0])}
            session.delete(order)
            session.commit()
            return response
        product = session.query(Products).get(id_product[0])
        if product is not None:
            if(quantity[0] < product.stock):
                price = product.price * quantity[0]
                product.stock = product.stock - quantity[0]
                session.add(product)
                detail = Details(id_orden, id_product[0], quantity[0], price)
                session.add(detail)
                try:
                    session.commit()
                    response = {"Resultado":"¡Guardado!"}
                    response = {"statusCode": 201, "body": json.dumps(response)}
                except Exception as e:
                    print(e)
                    response = {"Error":"Problemas con el servidor"}
                    response = {"statusCode": 500, "body": json.dumps(response)}
                    return response
            else:
                response = {"Error":f"No hay suficiente cantidad de {product.name}"}
                response = {"statusCode": 404, "body": json.dumps(response)}
                session.delete(order)
                session.commit()
                return response
        else:
            response = {"Error":"No existe el producto"}
            session.delete(order)
            session.commit()
            response = {"statusCode": 404, "body": json.dumps(response)}
            return response
    return response
        
        



