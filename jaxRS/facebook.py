from rauth import OAuth2Service

__author__ = 'tharinda'
# import classes
from backend.social.facebook import *
from backend.frontEndOperaions.indexOperations import *
# import libraries
from flask_restful import Resource
from backend.database.Operations import *
from flask import render_template, make_response, session

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
            session["facebook_user_token"] = getUserToken(flask.request.args.get("code"))
            getFacebookUserInfo(session["facebook_user_token"])
            session["facebookUser"] = json.loads(getFacebookUserJson())
            return flask.redirect(facebookConstants.returnURL)
        except NotAuthorizedException:
            return 'Access was not granted or authorization failed', 403
        except:
            raise


graph_url = 'https://graph.facebook.com/'
facebookAgent = OAuth2Service(name='facebook',
                              authorize_url='https://www.facebook.com/dialog/oauth',
                              access_token_url=graph_url + 'oauth/access_token',
                              client_id=facebookConstants.appID,
                              client_secret=facebookConstants.secretKey,
                              base_url=graph_url)


class facebookLogin(Resource):
    def get(self):
        facebookConstants.returnURL = flask.request.args.get("redirect")
        redirect_uri = REDIRECT_URI
        params = {'redirect_uri': redirect_uri}
        return flask.redirect(facebookAgent.get_authorize_url(**params))
class facebookAuthorized(Resource):
    def get(self):
        # make a request for the access token credentials using code
        redirect_uri = REDIRECT_URI
        data = dict(code=flask.request.args['code'], redirect_uri=redirect_uri)
        facebookSession = facebookAgent.get_auth_session(data=data)
        session["facebook_user_token"] = facebookSession.access_token
        getFacebookUserInfo(session["facebook_user_token"])
        session["facebookUser"] = json.loads(getFacebookUserJson())
        return flask.redirect(facebookConstants.returnURL)


class facebook(Resource):
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
                render_template('facebook/facebookPage.html', authorized=userAuthorized, id=userId,
                                name=userName, noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                                facebookPageNum=1, pageAppList=list),
                200, headers)


class getFacebookPage(Resource):
    def get(self, pageNum):
        global TOKENS, noOfAppsPagesFacebook, facebookUserObj, facebookAppCount, FacebookAppList
        facebookUserObj = getFacebookUser()
        startId, endId = getStartIdAndEndId(pageNum, facebookAppCount)
        list = getAppList(startId, endId, FacebookAppList, "facebook")
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
        return make_response(
                render_template('facebook/facebookPage.html', authorized=userAuthorized, id=userId,
                                name=userName, noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                                facebookPageNum=pageNum, pageAppList=list),
                200, headers)


class getFacebookApp(Resource):
    def get(self, appId):
        global TOKENS, facebookUserObj
        facebookCommentUrl = common.baseUrl + '/facebook/' + appId
        facebookUserObj = getFacebookUser()
        obj = getFacebookAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
        return make_response(
                render_template('facebook/facebookAppDetailPage.html', authorized=userAuthorized,
                                id=userId,
                                name=userName, appDetails=obj, facebookCommentUrl=facebookCommentUrl),
                200, headers)
