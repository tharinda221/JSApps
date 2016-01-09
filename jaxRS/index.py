__author__ = 'tharinda'
# import classes
from jaxRS.facebook import *
from backend.plainObjects.user import *
from backend.database.Operations import *
from backend.frontEndOperaions.indexOperations import *
# import libraries
from flask import Flask, make_response, render_template


# app = Flask(__name__)

class main(Resource):
    def get(self):
        global TOKENS
        global noOfAppsPagesFacebook
        startId, endId = facebookAppStartIdAndEndId(1)
        list = getAppList(startId, endId)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(render_template('index.html', authorized=userAuthorized, id=User.facebook.userId,
                                             name=User.facebook.userName, noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                                             facebookPageNum=1, pageAppList=list),
                             200, headers)


class getPage(Resource):
    def get(self, pageNum):
        global TOKENS
        global noOfAppsPagesFacebook
        startId, endId = facebookAppStartIdAndEndId(pageNum)
        list = getAppList(startId, endId)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(render_template('index.html', authorized=userAuthorized, id=User.facebook.userId,
                                             name=User.facebook.userName, noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                                             facebookPageNum=pageNum, pageAppList=list),
                             200, headers)


class getFacebookApp(Resource):
    def get(self, appId):
        global TOKENS
        obj = getAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(render_template('AppDetails.html', authorized=userAuthorized, id=User.facebook.userId,
                                             name=User.facebook.userName, appDetails=obj), 200, headers)
