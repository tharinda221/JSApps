from config import *
from backend.database.getDatabase import *


def __init__(self):
    pass


TOKENS = {}
twitterTokens = {"OAUTH_TOKEN": "", "OAUTH_TOKEN_SECRET": ""}


class common:
    def __init__(self):
        pass

    ApplicationSecret = ""
    numOfAppsPerPage = 8
    baseUrl = "http://" + host + ":" + str(port)
    # baseUrl = "http://jsapps.pythonanywhere.com"


class facebookConstants:
    def __init__(self):
        pass

    graphUrl = 'https://graph.facebook.com/'
    secretKey = "aa2bbf6cc9250e919a64292c6da9a447"
    appID = "954011938018310"
    GraphAPIVersion = "v2.5"
    redirectURL = common.baseUrl + "/callback/facebook"
    baseGraphApiUrl = "https://graph.facebook.com/v2.5/"
    getUserInitInfoUrl = "me?fields=name,birthday,about,bio,email,education,gender," \
                         "id,hometown"
    returnURL = ""


class twitterConstants:
    def __init__(self):
        pass

    REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
    AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
    ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

    CONSUMER_KEY = "idIKJAGhBQyhMYPPvctKYz17z"
    CONSUMER_SECRET = "5q5Nb7cK8DYyYeLNuzmm4RrIa9oEIympgQJ1vJo0337JbrdXDB"

    resource_owner_key = ""
    resource_owner_secret = ""
    returnURL = ""


class databaseCollections:
    def __init__(self):
        pass

    userFBCollectionName = getDatabase().facebookUsers
    userTwitterCollectionName = getDatabase().twitterUsers
    facebookAppsCollectionName = getDatabase().facebookApps
    twitterAppsCollectionName = getDatabase().twitterApps
