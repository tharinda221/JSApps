from rauth import OAuth2Service

# import classes
from werkzeug.utils import secure_filename

from backend.social.facebook import *
from backend.frontEndOperaions.indexOperations import *
# import libraries
from flask_restful import Resource
from backend.database.Operations import *
from flask import render_template, make_response, session, request

facebookAppCount = NumberOfFacebookApps()
FacebookAppList = getFacebookAppsIDList()


class createApp(Resource):
    def get(self):
        global facebookUserObj
        facebookUserObj = getFacebookUser()
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
        return make_response(
                render_template('facebook/userApp/createApp/createApp.html', authorized=userAuthorized, id=userId,
                                name=userName),
                200, headers)

    def post(self):
        global facebookUserObj
        print request.form
        file = request.files['watermark']
        filename = secure_filename(file.filename)
        filePath = config.facebookUserAppsImagePath + filename
        print filePath
        file.save(filePath)
        facebookUserObj = getFacebookUser()
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]