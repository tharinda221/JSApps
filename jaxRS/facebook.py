__author__ = 'tharinda'

import flask
from flask_restful import Resource
from backend.facebook import *
from json import  loads, dumps
import requests
class authorize_facebook(Resource):

    def get(self):
        return flask.redirect("https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&scope=publish_actions"
                        % (FACEBOOK_APP_ID, REDIRECT_URI))

class handle_callback(Resource):

    def get(self):
        global TOKENS
        try:
            TOKENS["user_token"] = get_user_token(flask.request.args.get("code"))

            return flask.redirect("/")
        except NotAuthorizedException:
            return 'Access was not granted or authorization failed', 403
        except:
            raise
class user_details(Resource):

    def get(self):
        user_authorized = True if "user_token" in TOKENS else False
        if(user_authorized):
            url = "https://graph.facebook.com/me?access_token=" + TOKENS["user_token"]
            response = requests.get(url)
            return response.json()
        else:
            dumps({'status': "401", 'message': "User not authorized"})