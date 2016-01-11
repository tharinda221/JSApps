__author__ = 'tharinda'
# import classes
from backend.social.facebook import *
from backend.apps.facebookApps import *
from backend.database.Operations import *
# import libraries
from flask_restful import Resource
from flask import make_response, render_template

runApplicaions = facebookAppsMethods()


class runFacebookApplication(Resource):
    def get(self, appId):
        obj = getFacebookAppDetailsById(appId)
        method_name = obj.AppMethodName
        method = getattr(runApplicaions, method_name)
        if not method:
            raise Exception("Method %s not implemented" % method_name)
        method()
        print "Finished"
        global TOKENS , facebookUserObj
        facebookUserObj = getFacebookUser()
        obj = getFacebookAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(render_template('facebook/facebookAppFinished.html', authorized=userAuthorized, id=facebookUserObj.userId,
                                             name=facebookUserObj.userName, appDetails=obj), 200, headers)
