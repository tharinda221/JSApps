# import classes
from backend.common.Constants import *
from backend.plainObjects.user import *
from backend.database.Operations import *

# import libraries
from twython import Twython
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from flask import session

CONSUMER_KEY = twitterConstants.CONSUMER_KEY
CONSUMER_SECRET = twitterConstants.CONSUMER_SECRET
twitterObj = User.twitterUser()


class NotAuthorizedException(Exception):
    pass


def getUserToken(verifier, resource_owner_key, resource_owner_secret):
    global twitterTokens
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)
    r = requests.post(url=twitterConstants.ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    return credentials.get('oauth_token')[0], credentials.get('oauth_token_secret')[0], credentials.get('screen_name')[
        0]


def getTwitterUserDetails(userToken, userSecret):
    twitterAgent = Twython(twitterConstants.CONSUMER_KEY, twitterConstants.CONSUMER_SECRET,
                           userToken,
                           userSecret)
    resp = twitterAgent.verify_credentials(screen_name=session["screen_name"])
    global twitterObj
    twitterObj = User.twitterUser(resp["id_str"],
                                  session["screen_name"],
                                  resp["name"],
                                  resp.get("geo", ""),
                                  resp.get("country", ""),
                                  resp["description"],
                                  resp['profile_image_url']
                                  )
    if getTwitterUserAvailability(session["screen_name"]):
        putTwitterUserData(userId=twitterObj.userId,
                           userScreenName=twitterObj.userScreenName,
                           userName=twitterObj.userName,
                           geoLocation=twitterObj.geoLocation,
                           country=twitterObj.country,
                           userDescription=twitterObj.userDescription,
                           profileImage=twitterObj.profileImage
                           )


def getTweetsToString(userToken, userSecret):
    re = ""
    twitterAgent = Twython(twitterConstants.CONSUMER_KEY, twitterConstants.CONSUMER_SECRET,
                           userToken,
                           userSecret)
    user_timeline = twitterAgent.get_user_timeline(screen_name=session["screen_name"], count=50)
    for tweet in user_timeline:
        # print tweet['text'] + "\n"
        re = re + tweet['text'] + " "
    return re


def getTwitterUser():
    return twitterObj


def getTwitterUserJson():
    return json.dumps(twitterObj, default=lambda o: o.__dict__)
