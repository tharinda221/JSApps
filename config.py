__author__ = 'tharinda'

# import libraries
import os
from flask import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
configDataPath = open(os.path.join(BASE_DIR, "JSApps/configuration/", "config.json"), "r")
configData = json.load(configDataPath)
host = configData["host"]
port = configData["port"]
database = configData["database"]
databaseName = configData["databaseName"]
AppsImagePath = BASE_DIR + "/JSApps/static/images/appImages/"
facebookUserAppsImagePath = BASE_DIR + "/JSApps/static/images/appImages/facebook/userApps/"
fontPath = BASE_DIR + "/JSApps/static/fonts/"
pathToStatic = BASE_DIR + "/JSApps/static/"
serverImagePath = "/home/ubuntu/JSApps/static/images/appImages/facebook/"
pathToUserImage = BASE_DIR + "/JSApps/static/images/appImages/facebook/userApps/"
pathToAppsImage = BASE_DIR + "/JSApps/static/images/appImages/facebook/"
