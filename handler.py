import json
import pymongo


def hello(event, context):
    n1 = int(event["pathParameters"]["n1"])
    n2 = int(event["pathParameters"]["n2"])
    sum = n1+n2

    return {
        "statusCode": 200,
        "body": sum  # json.dumps(body)
    }


def divide(event, context):
    try:
        n1 = int(event["pathParameters"]["n1"])
        n2 = int(event["pathParameters"]["n2"])
        div = n1/n2

        return {
            "statusCode": 200,
            "body": div  # json.dumps(0)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": "Can not divide by 0"
        }


def marks(event, context):
    n1 = int(event["pathParameters"]["n1"])
    n2 = int(event["pathParameters"]["n2"])
    n3 = int(event["pathParameters"]["n3"])
    total = n1+n2+n3
    ave = round(total/3, 2)
    dic = {"sum": total, "average": ave}
    return {
        "statusCode": 200,
        "body": json.dumps(dic)
    }


def qsDemo(event, context):
    name = event["queryStringParameters"]["name"]
    age = event["queryStringParameters"]["age"]
    return {
        "statusCode": 200,
        "body": json.dumps({
            "name": name,
            "age": age
        })
    }


def register(event, context):

    name = json.loads(event["body"])["name"]
    email = json.loads(event["body"])["email"]
    password = json.loads(event["body"])["password"]
    city = json.loads(event["body"])["city"]

    client = pymongo.MongoClient("mongodb+srv://vikas:vikas1@cluster0.vbdq2.mongodb.net")
    db = client["satyam-db"]
    collection = db["students"]

    collection.insert_one({
        "name": name,
        "email": email,
        "password": password,
        "city": city
    })

    return {
        "statusCode": 200,
        "body": "Regitration successful !"
    }


def getUser(event, context):
    # step1. Read email from query String Parameters
    email = event["queryStringParameters"]["email"]

    #DB
    client = pymongo.MongoClient("mongodb+srv://vikas:vikas1@cluster0.vbdq2.mongodb.net")
    db = client["satyam-db"]
    collection = db["students"]

    # find one from the collection with matching email id
    document = collection.find_one({"email": email})
    
    return {
        "statusCode": 200,
        "body": json.dumps(document, default=str)
    }
