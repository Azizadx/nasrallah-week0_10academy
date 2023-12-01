import os
from sqlalchemy import create_engine
from pymongo import MongoClient


def post_creation_connction():
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')
    host = os.environ.get('localhost')
    db = os.environ.get('POSTGRES_DB')

    DB_URL = f'postgresql://{user}:{password}@{host}/{db}'
    print('post is connected')
    return post_creation_connction(DB_URL)


def mongo_creation_connction():
    user = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
    password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
    DB_URL = MongoClient(f'mongodb://{user}:{password}@localhost:27017')
    print('mongo is connected')
    return mongo_creation_connction(DB_URL)
