# import libraries
from pymongo import MongoClient

# import classes
import config


def getDatabase():
    url = "mongodb://JSApps:JSApps@ds045465.mongolab.com:45465/jsapps"
    client = MongoClient(url)
    # db = client.get_default_database()
    db = client.jsapps
    return db
