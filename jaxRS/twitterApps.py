__author__ = 'tharinda'
# import classes
from backend.social.twitter import *
from backend.database.Operations import *
from backend.apps.twitterApps import *
# import libraries
from flask_restful import Resource
from flask import make_response, render_template

runTwitterApp = twitterAppsMethods()


class runTwitterApplicaions(Resource):
    def get(self, appId):
        obj = getTwitterAppDetailsById(appId)
        method_name = obj.AppMethodName
        method = getattr(runTwitterApp, method_name)
        if not method:
            raise Exception("Method %s not implemented" % method_name)
        method()
        print "Finished"
        global twitterTokens, twitterObj
        twitterObj = getTwitterUser()
        obj = getTwitterAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        twitterUserAuthorized = True if "twitterToken" in twitterTokens else False
        return make_response(render_template('twitter/twitterAppFinished.html', TwitterAuthorized=twitterUserAuthorized,
                                             profilePicture=twitterObj.profileImage,
                                             name=twitterObj.userName, appDetails=obj), 200, headers)
