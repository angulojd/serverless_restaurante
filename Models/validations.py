import re
import json

#Validar datos del usuario que no esten repetidos
def val_user_repet(e):
    if('user.phone' in str(e)):
        response = {"Error":"Telefono ya registrado en otra cuenta"}
    elif('user.email' in str(e)):
        response = {"Error":"Email ya registrado en otra cuenta"}
    elif('user.username' in str(e)):
        response = {"Error":"Username ya registrado en otra cuenta"}
    response = {"statusCode": 401, "body": json.dumps(response)}
    return response

#Validar que el json este bien estructurado
def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

#Validar que la variable tenga solo numeros
def val_number(number, data):
    reg_exp = "[-+]?\d+$"
    try:
        number = int(number)
        return number, True
    except Exception as e:
        if(re.match(reg_exp, number)):
            if(int(number) > -1):
                return int(number), True
            else:
                return {"Error":f"la variable {data} tiene caracteres"}, False
        else:
            return {"Error":f"la variable {data} tiene caracteres"}, False

#Verifica que la variable sea un email
def val_email(email):
    if("@" not in email or "." not in email):
        return {"Error":"la variable email no es un correo"}, False
    else:
        return email, True
    
