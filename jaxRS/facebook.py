__author__ = 'tharinda'
# import classes
from backend.social.facebook import *
# import libraries
from flask_restful import Resource


class authorizeFacebook(Resource):
    def get(self):
        return flask.redirect("https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&scope=publish_actions"
                              % (FACEBOOK_APP_ID, REDIRECT_URI))


class handleCallback(Resource):
    def get(self):
        global TOKENS
        global USER
        try:
            TOKENS["user_token"] = getUserToken(flask.request.args.get("code"))
            USER["id"] = getUserInitInfo(TOKENS["user_token"])['id']
            USER["name"] = getUserInitInfo(TOKENS["user_token"])['name']
            return flask.redirect("/")
        except NotAuthorizedException:
            return 'Access was not granted or authorization failed', 403
        except:
            raise
