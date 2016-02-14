__author__ = 'tharinda'
# import classes
from backend.social.facebook import *
from backend.apps.facebookApps import *
from backend.database.Operations import *
# import libraries
from flask_restful import Resource
from flask import make_response, render_template, request

runApplicaions = facebookAppsMethods()


class runFacebookApplication(Resource):
    def get(self, appId):
        userAuthorized = True if "facebook_user_token" in session else False
        if userAuthorized:
            obj = getFacebookAppDetailsById(appId)
            # run method
            method_name = obj.AppMethodName
            method = getattr(runApplicaions, method_name)
            if not method:
                raise Exception("Method %s not implemented" % method_name)
            method(appId)
            print "Finished"
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
            facebookCommentUrl = common.baseUrl + '/facebook/' + appId
            obj = getFacebookAppDetailsById(appId)
            headers = {'Content-Type': 'text/html'}

            return make_response(
                render_template('facebook/facebookAdminApp/facebookAppFinished.html', authorized=userAuthorized,
                                id=userId,
                                name=userName, appDetails=obj,
                                facebookCommentUrl=facebookCommentUrl), 200, headers)
        else:
            return flask.redirect('/facebook/appDetails/' + appId)


class runFacebookUserApplication(Resource):
    def get(self, appId):
        userAuthorized = True if "facebook_user_token" in session else False
        if userAuthorized:
            obj = getFacebookUserCreatableAppDetailsById(appId)
            # run method
            method_name = obj.AppMethodName
            method = getattr(runApplicaions, method_name)
            if not method:
                raise Exception("Method %s not implemented" % method_name)
            session["image"] = method(appId)
            print "Finished"
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
            facebookCommentUrl = common.baseUrl + '/facebook/' + appId
            obj = getFacebookAppDetailsById(appId)
            headers = {'Content-Type': 'text/html'}

            return make_response(
                render_template('facebook/facebookAdminApp/facebookAppFinished.html', authorized=userAuthorized,
                                id=userId,
                                name=userName, appDetails=obj,
                                facebookCommentUrl=facebookCommentUrl, image=session["image"]), 200, headers)
        else:
            return flask.redirect('/facebook/appDetails/userApp' + appId)
