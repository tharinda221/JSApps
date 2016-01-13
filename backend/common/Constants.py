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
    baseUrl = "http://" + host + ":" + str(port) + "/"


class facebookConstants:
    def __init__(self):
        pass

    secretKey = "810caf413c4786364eb65172fed5a03c"
    appID = "1672045909732059"
    GraphAPIVersion = "v2.5"
    # redirectURL = "http://" + host + ":" + str(port) + "/callback/facebook"
    redirectURL = "http://tharinda221.pythonanywhere.com/callback/facebook"
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
    screen_name = ""
    returnURL = ""


class databaseCollections:
    def __init__(self):
        pass

    userFBCollectionName = getDatabase().facebookUsers
    userTwitterCollectionName = getDatabase().twitterUsers
    facebookAppsCollectionName = getDatabase().facebookApps
    twitterAppsCollectionName = getDatabase().twitterApps
