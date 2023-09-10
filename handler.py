import json
import Models.db2 as db2
from Models.validations import json_validator
from Services.createProduct import save_product, update_product
from Services.createUser import save_user
from Services.createOrder import save_order
from Services.createCategory import save_category
from Services.reports import report_product

def user(event, context):
    if(json_validator(event['body'])):
        data = json.loads(event['body'])
        response = save_user(data)
        return response
    else:
        response = {"Error":"invalid json"}
        response = {"statusCode": 500, "body": json.dumps(response)}
        return response

def product(event, context):
    if(json_validator(event['body'])):
        data = json.loads(event['body'])
        response = save_product(data)
        return response
    else:
        response = {"Error":"invalid json"}
        response = {"statusCode": 500, "body": json.dumps(response)}
        return response

def order(event, context):
    if(json_validator(event['body'])):
        data = json.loads(event['body'])
        response = save_order(data)
        return response
    else:
        response = {"Error":"invalid json"}
        response = {"statusCode": 500, "body": json.dumps(response)}
        return response

def category(event, context):
    if(json_validator(event['body'])):
        data = json.loads(event['body'])
        response = save_category(data)
        return response
    else:
        response = {"Error":"invalid json"}
        response = {"statusCode": 500, "body": json.dumps(response)}
        return response

def updateProduct(event, context):
    if(json_validator(event['body'])):
        data = json.loads(event['body'])
        response = update_product(data)
        return response
    else:
        response = {"Error":"invalid json"}
        response = {"statusCode": 500, "body": json.dumps(response)}
        return response

def report(event, context):
    response = report_product()
    return response

if __name__ == '__main__':
    db2.Base.metadata.drop_all(db2.engine)
    db2.Base.metadata.create_all(db2.engine)
