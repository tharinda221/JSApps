# import classes
from backend.common.Constants import *

# import libraries
from twython import Twython
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs

CONSUMER_KEY = twitter.CONSUMER_KEY
CONSUMER_SECRET = twitter.CONSUMER_SECRET


class NotAuthorizedException(Exception):
    pass


def getUserToken(verifier):
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=twitter.resource_owner_key,
                   resource_owner_secret=twitter.resource_owner_secret,
                   verifier=verifier)

    r = requests.post(url=twitter.ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    twitterTokens["twitterToken"] = credentials.get('oauth_token')[0]
    twitterTokens["twitterSecret"] = credentials.get('oauth_token_secret')[0]
    twitter.screen_name = credentials.get('screen_name')[0]


def getUserDetails():
    twitterAgent = Twython(twitter.CONSUMER_KEY, twitter.CONSUMER_SECRET, twitterTokens["OAUTH_TOKEN"],
                           twitterTokens["OAUTH_TOKEN_SECRET"])
    # resp = twitterAgent.show_user(screen_name=twitter.screen_name)
    resp= twitterAgent.get_user_timeline(screen_name=twitter.screen_name, count=50)
    for tweet in resp:
        print tweet['text'] + "\n"
    return resp
