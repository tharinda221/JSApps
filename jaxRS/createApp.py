from rauth import OAuth2Service

# import classes
from backend.social.facebook import *
from backend.frontEndOperaions.indexOperations import *
# import libraries
from flask_restful import Resource
from backend.database.Operations import *
from flask import render_template, make_response, session

facebookAppCount = NumberOfFacebookApps()
FacebookAppList = getFacebookAppsIDList()

class createApp(Resource):
    def get(self):
        global TOKENS, noOfAppsPagesFacebook, facebookUserObj, facebookAppCount, FacebookAppList
        facebookUserObj = getFacebookUser()
        startId, endId = getStartIdAndEndId(1, facebookAppCount)
        list = getAppList(startId, endId, FacebookAppList, "facebook")
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
        return make_response(
                render_template('facebook/userApp/createApp/createApp.html', authorized=userAuthorized, id=userId,
                                name=userName, noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                                facebookPageNum=1, pageAppList=list),
                200, headers)
