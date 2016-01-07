# import libraries
import flask
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from flask_restful import Resource

# import classes
from backend.common.Constants import *
from backend.social.twitter import *

REQUEST_TOKEN_URL = twitter.REQUEST_TOKEN_URL
AUTHORIZE_URL = twitter.AUTHORIZE_URL
ACCESS_TOKEN_URL = twitter.REQUEST_TOKEN_URL

CONSUMER_KEY = twitter.CONSUMER_KEY
CONSUMER_SECRET = twitter.CONSUMER_SECRET


class authorizeTwitter(Resource):
    def get(self):
        oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
        r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
        credentials = parse_qs(r.content)

        twitter.resource_owner_key = credentials.get('oauth_token')[0]
        twitter.resource_owner_secret = credentials.get('oauth_token_secret')[0]

        # Authorize
        authorize_url = AUTHORIZE_URL + twitter.resource_owner_key
        return flask.redirect(authorize_url)


class handleCallbackTwitter(Resource):
    def get(self):
        try:
            verifier = flask.request.args.get("oauth_verifier")
            getUserToken(verifier)
            return flask.redirect("/")

        except NotAuthorizedException:
            return 'Access was not granted or authorization failed', 403
        except:
            raise
