# import classes
from backend.common.Constants import *
from backend.plainObjects.user import *
from backend.database.Operations import *
# import libraries
from twython import Twython
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs

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
    twitterTokens["twitterToken"] = credentials.get('oauth_token')[0]
    twitterTokens["twitterSecret"] = credentials.get('oauth_token_secret')[0]
    twitterConstants.screen_name = credentials.get('screen_name')[0]


def getTwitterUserDetails():
    twitterAgent = Twython(twitterConstants.CONSUMER_KEY, twitterConstants.CONSUMER_SECRET, twitterTokens["twitterToken"],
                           twitterTokens["twitterSecret"])
    resp = twitterAgent.verify_credentials(screen_name=twitterConstants.screen_name)
    global twitterObj
    twitterObj = User.twitterUser(resp["id_str"],
                                  twitterConstants.screen_name,
                                  resp["name"],
                                  resp.get("geo", ""),
                                  resp.get("country", ""),
                                  resp["description"],
                                  resp['profile_image_url']
                                  )
    if getTwitterUserAvailability(twitterConstants.screen_name):
        putTwitterUserData(userId=twitterObj.userId,
                           userScreenName=twitterObj.userScreenName,
                           userName=twitterObj.userName,
                           geoLocation=twitterObj.geoLocation,
                           country=twitterObj.country,
                           userDescription=twitterObj.userDescription,
                           profileImage=twitterObj.profileImage
                           )


def getTwitterUser():
    return twitterObj
