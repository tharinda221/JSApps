__author__ = 'tharinda'

# import classes
from backend.common.Constants import *
from backend.plainObjects.user import *
from backend.database.Operations import *
# import libraries
import urllib
from json import loads
from urllib3 import HTTPSConnectionPool
from urlparse import parse_qs
import requests
import logging
import flask

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.secret_key = common.ApplicationSecret

FACEBOOK_APP_ID = facebookConstants.appID
FACEBOOK_APP_SECRET = facebookConstants.secretKey
GRAPH_API_VERSION = facebookConstants.GraphAPIVersion
REDIRECT_URI = facebookConstants.redirectURL
returnURL = facebookConstants.returnURL

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
requests.packages.urllib3.disable_warnings()

facebookUserObj = User.facebookUser()


class NotAuthorizedException(Exception):
    pass


class FacebookConnection(HTTPSConnectionPool):
    def __init__(self):
        super(FacebookConnection, self).__init__('graph.facebook.com')

    def __call__(self, method, url, token, http_headers, request_body):
        if http_headers is None:
            http_headers = {}

        if token is not None:
            http_headers["Authorization"] = "Bearer %s" % token

        return self.urlopen(method, url, headers=http_headers, body=request_body)


FACEBOOK_CONNECTION = FacebookConnection()


# OAuth functions

def GetAppToken():
    try:
        response = FACEBOOK_CONNECTION(
                'GET',
                '/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials'
                % (FACEBOOK_APP_ID, FACEBOOK_APP_SECRET),
                None, None, None)

        return parse_qs(response.data.decode("utf-8"))["access_token"]
    except KeyError:
        logging.log(logging.ERROR, response.data)
        raise NotAuthorizedException("Authorization error", "App access token not found")
    except:
        raise


def getUserToken(code):
    try:
        response = FACEBOOK_CONNECTION(
                'GET',
                '/%s/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s'
                % (GRAPH_API_VERSION, FACEBOOK_APP_ID, REDIRECT_URI, FACEBOOK_APP_SECRET, code),
                None, None, None)
        return loads(response.data.decode("utf-8"))["access_token"]
    except KeyError:
        logging.log(logging.ERROR, response.data)
        raise NotAuthorizedException("Authorization error", "User access token not found")
    except:
        raise


def getFacebookUserInfo(accesstoken):
    url = facebookConstants.baseGraphApiUrl + facebookConstants.getUserInitInfoUrl + "&access_token=" + \
          accesstoken + ""
    response = json.load(urllib.urlopen(url))
    global facebookUserObj
    facebookUserObj = User.facebookUser(userId=response.get("id", ""),
                                        userName=response.get("name", ""),
                                        gender=response.get("gender", ""),
                                        birthDay=response.get("birthday", ""),
                                        hometown=response.get("hometown", ""),
                                        email=response.get("email", ""),
                                        education=response.get("education", []),
                                        about=response.get("about", ""))
    if getFacebookUserAvailability(facebookUserObj.userId):
        putFacebookUserData(userId=facebookUserObj.userId,
                            userName=facebookUserObj.userName,
                            gender=facebookUserObj.gender,
                            birthDay=facebookUserObj.birthDay,
                            hometown=facebookUserObj.hometown,
                            email=facebookUserObj.email,
                            education=facebookUserObj.education,
                            about=facebookUserObj.about)


def getFacebookUser():
    return facebookUserObj


def getAllAlbums(accesstoken, uid):
    url = facebookConstants.baseGraphApiUrl + uid + "/albums?access_token=" + accesstoken + ""
    return json.load(urllib.urlopen(url))


def getAlbumIdByName(accesstoken, uid, name):
    response = getAllAlbums(accesstoken, uid)
    for data in response["data"]:
        if data["name"] == name:
            return data["id"]
    return "name not found"


def getAlbumFromId(accesstoken, id):
    url = facebookConstants.baseGraphApiUrl + id + "/photos?fields=name,source,id,created_time" + "&access_token=" + \
          accesstoken + ""
    return json.load(urllib.urlopen(url))
