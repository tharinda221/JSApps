__author__ = 'tharinda'
# import classes
from backend.social.facebook import *
from backend.frontEndOperaions.indexOperations import *
# import libraries
from flask_restful import Resource
from backend.database.Operations import *
from flask import render_template, make_response

facebookAppCount = NumberOfFacebookApps()
FacebookAppList = getFacebookAppsIDList()

class authorizeFacebook(Resource):
    def get(self):
        facebookConstants.returnURL = flask.request.args.get("redirect")
        return flask.redirect("https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&scope=publish_actions"
                              % (FACEBOOK_APP_ID, REDIRECT_URI))


class handleCallbackFacebook(Resource):
    def get(self):
        global TOKENS
        global USER
        try:
            TOKENS["user_token"] = getUserToken(flask.request.args.get("code"))
            getFacebookUserInfo(TOKENS["user_token"])

            return flask.redirect(facebookConstants.returnURL)
        except NotAuthorizedException:
            return 'Access was not granted or authorization failed', 403
        except:
            raise


class facebook(Resource):
    def get(self):
        global TOKENS, noOfAppsPagesFacebook, facebookUserObj, facebookAppCount, FacebookAppList
        facebookUserObj = getFacebookUser()
        startId, endId = getStartIdAndEndId(1, facebookAppCount)
        list = getAppList(startId, endId, FacebookAppList, "facebook")
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(
            render_template('facebook/facebookPage.html', authorized=userAuthorized, id=facebookUserObj.userId,
                            name=facebookUserObj.userName, noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                            facebookPageNum=1, pageAppList=list),
            200, headers)


class getFacebookPage(Resource):
    def get(self, pageNum):
        global TOKENS, noOfAppsPagesFacebook, facebookUserObj, facebookAppCount, FacebookAppList
        facebookUserObj = getFacebookUser()
        startId, endId = getStartIdAndEndId(pageNum, facebookAppCount)
        list = getAppList(startId, endId, FacebookAppList, "facebook")
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(
            render_template('facebook/facebookPage.html', authorized=userAuthorized, id=facebookUserObj.userId,
                            name=facebookUserObj.userName, noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                            facebookPageNum=pageNum, pageAppList=list),
            200, headers)


class getFacebookApp(Resource):
    def get(self, appId):
        global TOKENS, facebookUserObj
        facebookUserObj = getFacebookUser()
        obj = getFacebookAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(
            render_template('facebook/facebookAppDetailPage.html', authorized=userAuthorized, id=facebookUserObj.userId,
                            name=facebookUserObj.userName, appDetails=obj), 200, headers)
