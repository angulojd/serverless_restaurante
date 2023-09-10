import json
from Models.validations import val_number
from Models.db2 import session
from Models.orders import Orders
from Models.users import Users
from Services.createOrderDetails import save_details

def save_order(data):
        id_user = val_number(data["id_user"], "id_user")
        if id_user[1] is False:
            response = {"statusCode": 400, "body": json.dumps(id_user[0])}
            return response
        postal = val_number(data["postal"], "postal")
        if postal[1] is False:
            response = {"statusCode": 400, "body": json.dumps(postal[0])}
            return response
        name = str(data["name"])
        if session.query(Users).get(id_user[0]) is not None:
            order = Orders(id_user[0], None ,postal[0])
        else:
            order = Orders(None, name, postal[0])
        details = data["pedidos"]
        session.add(order)
        try:
            session.commit()
            details = data["pedidos"]
            response = save_details(details, order.id, order)
        except Exception as e:
            response = {"Error":"Problemas con el servidor"}
            response = {"statusCode": 500, "body": json.dumps(response)}
        return response
