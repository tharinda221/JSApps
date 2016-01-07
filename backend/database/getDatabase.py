# import libraries
from pymongo import MongoClient

# import classes
import config


def getDatabase():
    client = MongoClient(config.database)
    db = client[config.databaseName]
    return db
