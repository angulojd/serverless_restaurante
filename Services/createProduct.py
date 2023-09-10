import json
from Models.products import Products
from Models.category import Categories
from Models.validations import val_number
from datetime import datetime
from Models.db2 import session

def save_product(data):
    name = str(data['name'])
    price = val_number(data['price'], "price")
    stock = val_number(data['stock'], "stock")
    id_category = val_number(data['id_category'], "id_category")
    if price[1] is False:
        response = {"statusCode": 400, "body": json.dumps(price[0])}
        return response
    elif stock[1] is False:
        response = {"statusCode": 400, "body": json.dumps(stock[0])}
        return response
    elif id_category[1] is False:
        response = {"statusCode": 400, "body": json.dumps(id_category[0])}
        return response
    else:
        if session.query(Categories).get(id_category[0]) is not None:
            product = Products(name, price[0], stock[0], id_category[0])
            session.add(product)
            try:
                session.commit()
                response = {"Resultado":"¡Guardado!"}
                response = {"statusCode": 201, "body": json.dumps(response)}
            except Exception as e:
                response = {"Error":"Problemas con el servidor"}
                response = {"statusCode": 500, "body": json.dumps(response)}
                return response
        else:
            response = {"Error":"Categoria inexistente"}
            response = {"statusCode": 400, "body": json.dumps(response)}
            return response
    return response

def update_product(data):
    sw = False
    try:
        price = val_number(data["price"], "price")
        if price[1] is False:
            response = {"statusCode": 400, "body": json.dumps(price[0])}
            return response
        stock = val_number(data["stock"], "stock")
        if stock[1] is False:
            response = {"statusCode": 400, "body": json.dumps(stock[0])}
            return response
        sw = True
    except Exception as e:
        if('price' in str(e)):
            stock = val_number(data["stock"], "stock")
            price = False
            if stock[1] is False:
                response = {"statusCode": 400, "body": json.dumps(stock[0])}
                return response
        elif('stock' in str(e)):
            price = val_number(data["price"], "price")
            stock = False
            if price[1] is False:
                response = {"statusCode": 400, "body": json.dumps(price[0])}
                return response
    id_product = val_number(data["id_product"], "id_product")
    if id_product[1] is False:
        response = {"statusCode": 400, "body": json.dumps(id_product[0])}
        return response
    else:
        product = session.query(Products).get(id_product[0])
        if product is not None:
            if(price or sw):
                product.price = price[0]
            if(stock or sw):
                product.stock = product.stock + int(stock[0])
            product.update_at = datetime.now()
            session.add(product)
            session.commit()
            response = {"Resultado":"¡Guardado!"}
            response = {"statusCode": 200, "body": json.dumps(response)}
        else:
            response = {"Error":"Producto inexistente"}
            response = {"statusCode": 404, "body": json.dumps(response)}
    return response