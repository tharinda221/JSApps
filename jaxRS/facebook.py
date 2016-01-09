__author__ = 'tharinda'
# import classes
from backend.social.facebook import *
# import libraries
from flask_restful import Resource
from backend.database.Operations import *

class authorizeFacebook(Resource):
    def get(self):
        facebook.returnURL = flask.request.args.get("redirect")
        return flask.redirect("https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&scope=publish_actions"
                              % (FACEBOOK_APP_ID, REDIRECT_URI))


class handleCallbackFacebook(Resource):
    def get(self):
        global TOKENS
        global USER
        try:
            TOKENS["user_token"] = getUserToken(flask.request.args.get("code"))
            getUserInitInfo(TOKENS["user_token"])
            #putUserData()

            return flask.redirect(facebook.returnURL)
        except NotAuthorizedException:
            return 'Access was not granted or authorization failed', 403
        except:
            raise
