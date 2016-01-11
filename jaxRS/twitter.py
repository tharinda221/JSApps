# import libraries
import flask
from flask import render_template, make_response
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from flask_restful import Resource

# import classes
from backend.common.Constants import *
from backend.social.twitter import *
from backend.frontEndOperaions.indexOperations import *

REQUEST_TOKEN_URL = twitter.REQUEST_TOKEN_URL
AUTHORIZE_URL = twitter.AUTHORIZE_URL
ACCESS_TOKEN_URL = twitter.REQUEST_TOKEN_URL

CONSUMER_KEY = twitter.CONSUMER_KEY
CONSUMER_SECRET = twitter.CONSUMER_SECRET
resource_owner_key = twitter.resource_owner_key
resource_owner_secret = twitter.resource_owner_secret


class authorizeTwitter(Resource):
    def get(self):
        global resource_owner_key, resource_owner_secret
        twitter.returnURL = flask.request.args.get("redirect")
        oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
        r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
        credentials = parse_qs(r.content)
        resource_owner_key = credentials.get('oauth_token')[0]
        resource_owner_secret = credentials.get('oauth_token_secret')[0]

        # Authorize
        authorize_url = AUTHORIZE_URL + resource_owner_key
        return flask.redirect(authorize_url)


class handleCallbackTwitter(Resource):
    def get(self):
        try:
            verifier = flask.request.args.get("oauth_verifier")
            getUserToken(verifier, resource_owner_key, resource_owner_secret)
            getTwitterUserDetails()
            return flask.redirect(twitter.returnURL)

        except NotAuthorizedException:
            return 'Access was not granted or authorization failed', 403
        except:
            raise


class twitter(Resource):
    def get(self):
        global twitterTokens
        global noOfAppsPagesTwitter
        twitterObj = getTwitterUser()
        startId, endId = twitterAppStartIdAndEndId(1)
        list = getTwitterAppList(startId, endId)
        headers = {'Content-Type': 'text/html'}
        twitterUserAuthorized = True if "twitterToken" in twitterTokens else False
        return make_response(render_template('TwitterPage.html', TwitterAuthorized=twitterUserAuthorized,
                                             profilePicture=twitterObj.profileImage,
                                             name=twitterObj.userName, noOfAppsPagesTwitter=noOfAppsPagesTwitter,
                                             twitterPageNum=1, pageTwitterAppList=list),
                             200, headers)


class getTwitterPage(Resource):
    def get(self, pageNum):
        global twitterTokens
        global noOfAppsPagesTwitter
        global twitterObj
        startId, endId = twitterAppStartIdAndEndId(pageNum)
        list = getTwitterAppList(startId, endId)
        headers = {'Content-Type': 'text/html'}
        if twitterTokens["OAUTH_TOKEN"] == "":
            twitterUserAuthorized = False
        else:
            twitterUserAuthorized = True
        return make_response(
                render_template('TwitterPage.html', TwitterAuthorized=twitterUserAuthorized, id=User.twitterUser.userId,
                                name=User.twitterUser.userName, noOfAppsPagesTwitter=noOfAppsPagesTwitter,
                                twitterPageNum=1, pageTwitterAppList=list),
                200, headers)


class getTwitterApp(Resource):
    def get(self, appId):
        global TOKENS
        global twitterObj
        obj = getFacebookAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(render_template('AppDetails.html', authorized=userAuthorized, id=User.facebook.userId,
                                             name=User.facebook.userName, appDetails=obj), 200, headers)
