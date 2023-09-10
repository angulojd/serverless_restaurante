import json
from Models.db2 import session
from Models.users import Users
from Models.validations import val_number, val_user_repet, val_email

def save_user(data):
        username = str(data["username"])
        firstname = str(data["firstname"])
        lastname = str(data["lastname"])
        email = val_email(str(data["email"]))
        phone = val_number(data["phone"], "phone")
        if email[1] is False:
            response = {"statusCode": 400, "body": json.dumps(email[0])}
            return response
        elif phone[1] is False:
            response = {"statusCode": 400, "body": json.dumps(phone[0])}
            return response
        else:
            user = Users(username, firstname, lastname, email[0], int(phone[0]))
            session.add(user)
            try:
                session.commit()
                response = {"Resultado":"¡Guardado!"}
                response = {"statusCode": 201, "body": json.dumps(response)}
            except Exception as e:
                session.close()
                response = val_user_repet(str(e))
        return response


