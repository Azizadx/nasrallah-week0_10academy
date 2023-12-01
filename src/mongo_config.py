import os
from pymongo import MongoClient


def mongo_creation_connction():
    user = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
    password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
    DB_URL = MongoClient(f'mongodb://{user}:{password}@localhost:27017')
    print('mongo is connected')
    return mongo_creation_connction(DB_URL)
