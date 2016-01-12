__author__ = 'tharinda'
# import classes
from backend.social.twitter import *
from backend.database.Operations import *
from backend.apps.twitterApps import *
# import libraries
from flask_restful import Resource
from flask import make_response, render_template, request
import flask

runTwitterApp = twitterAppsMethods()


class runTwitterApplicaions(Resource):
    def get(self, appId):
        global twitterTokens
        twitterUserAuthorized = True if "twitterToken" in twitterTokens else False
        if twitterUserAuthorized:
            obj = getTwitterAppDetailsById(appId)
            # run method
            method_name = obj.AppMethodName
            method = getattr(runTwitterApp, method_name)
            if not method:
                raise Exception("Method %s not implemented" % method_name)
            method()
            print "Finished"
            global twitterObj
            twitterObj = getTwitterUser()
            twitterCommentUrl = common.baseUrl + '/twitter/' + appId
            obj = getTwitterAppDetailsById(appId)
            headers = {'Content-Type': 'text/html'}
            return make_response(
                    render_template('twitter/twitterAppFinished.html', TwitterAuthorized=twitterUserAuthorized,
                                    profilePicture=twitterObj.profileImage,
                                    name=twitterObj.userName, appDetails=obj, twitterCommentUrl=twitterCommentUrl), 200,
                    headers)
        else:
            return flask.redirect('/twitter/appDetails/' + appId)
