from pymongo import MongoClient
import os

MONGODB_URI = os.environ.get('MONGODB_URI')
if MONGODB_URI is None:
    MONGODB_URI = 'mongodb://localhost:27017'

__connection_map = {}

def get_collection(dbname, collection):
    if dbname not in __connection_map.keys():
        __connection_map[dbname] = MongoClient(MONGODB_URI)[dbname]
    return __connection_map.get(dbname)[collection]

def drop_database(dbname):
    MongoClient(MONGODB_URI).drop_database(dbname)

def get_client():
    return MongoClient(MONGODB_URI)

