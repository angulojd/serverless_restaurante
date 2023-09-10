import json
from Models.db2 import session
from Models.category import Categories

def save_category(data):
    name = str(data["name"])
    description = str(data["description"])
    category = Categories(name, description)
    session.add(category)
    try:
        session.commit()
        response = {"Resultado":"¡Guardado!"}
        response = {"statusCode": 201, "body": json.dumps(response)}
    except Exception as e:
        response = {"Error":"Problemas con el servidor"}
        response = {"statusCode": 500, "body": json.dumps(response)}
    return response