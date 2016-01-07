__author__ = 'tharinda'

# import classes
from backend.common.Constants import *
from backend.plainObjects.user import *
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

FACEBOOK_APP_ID = facebook.appID
FACEBOOK_APP_SECRET = facebook.secretKey
GRAPH_API_VERSION = facebook.GraphAPIVersion
REDIRECT_URI = facebook.redirectURL

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
requests.packages.urllib3.disable_warnings()


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


def getUserInitInfo(accesstoken):
    url = facebook.baseGraphApiUrl + facebook.getUserInitInfoUrl + "&access_token=" + \
          accesstoken + ""
    response = json.load(urllib.urlopen(url))
    User.facebook.userId = response.get("id", "")
    User.facebook.userName = response.get("name", "")
    User.facebook.email = response.get("email", "")
    User.facebook.gender = response.get("gender", "")
    User.facebook.birthDay = response.get("birthday", "")
    User.facebook.hometown = response.get("hometown", "")
    User.facebook.education = response.get("education", [])
    User.facebook.about = response.get("about", "")


def getAllAlbums(accesstoken, uid):
    url = facebook.baseGraphApiUrl + uid + "/albums?access_token=" + accesstoken + ""
    return json.load(urllib.urlopen(url))


def getAlbumIdByName(accesstoken, uid, name):
    response = getAllAlbums(accesstoken, uid)
    for data in response["data"]:
        if data["name"] == name:
            return data["id"]
    return "name not found"


def getAlbumFromId(accesstoken, id):
    url = facebook.baseGraphApiUrl + id + "/photos?fields=name,source,id,created_time" + "&access_token=" + \
          accesstoken + ""
    return json.load(urllib.urlopen(url))
