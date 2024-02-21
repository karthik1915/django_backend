import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

# importing connection string from .env
load_dotenv()
mongodb_connection_string = os.getenv("MONGODB_CONNECTION_STRING")
url = mongodb_connection_string

# function to ping mongodb


def PingMongo():
    client = MongoClient(url, server_api=ServerApi("1"))
    try:
        client.admin.command("ping")
        return True
    except Exception as e:
        return False

# function to fetch all data


def fetchalldata(collection_name, dbname="foodapp") -> list:
    data_array = []
    client = MongoClient(url)
    db = client[dbname]
    collection = db[collection_name]
    data = collection.find({})
    for i in data:
        i["_id"] = str(i["_id"])
        data_array.append(i)
    return data_array


def fetchdatabyid(collection_name, id, dbname="foodapp") -> object:
    client = MongoClient(url)
    db = client[dbname]
    collection = db[collection_name]
    data = collection.find_one({"_id": ObjectId(id)})
    data["_id"] = str(data["_id"])
    return data


def fetchdatabyquery(collection_name, query, dbname="foodapp") -> object:
    client = MongoClient(url)
    db = client[dbname]
    collection = db[collection_name]
    cursor = collection.find(query)
    return list(cursor)


def insertdata(collection_name, data, dbname="foodapp"):
    client = MongoClient(url)
    db = client[dbname]
    collection = db[collection_name]
    collection.insert_one(data)


def deletedatabyid(collection_name, id, dbname="foodapp") -> int:
    client = MongoClient(url)
    db = client[dbname]
    collection = db[collection_name]
    result = collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count


def insertmanydocuments(collection_name, data, dbname="foodapp"):
    client = MongoClient(url)
    db = client[dbname]
    collection = db[collection_name]
    collection.insert_many(data)


def deletemanydocuments(collection_name, data, dbname="foodapp"):
    client = MongoClient(url)
    db = client[dbname]
    collection = db[collection_name]
    ids = data
    objids = [ObjectId(id) for id in ids]
    filter = {"_id": {"$in": objids}}
    collection.delete_many(filter)
