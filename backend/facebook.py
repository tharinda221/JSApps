__author__ = 'tharinda'

from json import loads, dumps
from urllib3 import HTTPSConnectionPool
from urlparse import parse_qs

import requests

import logging
import flask

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "cb5fcc9d29666ecb06ef35f9bdeddc54"
#Bootstrap(app)

FACEBOOK_APP_ID="1061202120578874"
FACEBOOK_APP_SECRET="cb5fcc9d29666ecb06ef35f9bdeddc54"
GRAPH_API_VERSION="v2.4"
REDIRECT_URI="http://localhost:8080/callback"

TOKENS = {}

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

FACEBOOK_CONNECTION=FacebookConnection()

# OAuth functions


def get_app_token():

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


def get_user_token(code):
    try:
        response = FACEBOOK_CONNECTION(
            'GET',
            '/%s/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s'
            % (GRAPH_API_VERSION, FACEBOOK_APP_ID, REDIRECT_URI, FACEBOOK_APP_SECRET, code),
            None, None, None)
        print(response.data.decode("utf-8"))

        return loads(response.data.decode("utf-8"))["access_token"]
    except KeyError:
        logging.log(logging.ERROR, response.data)
        raise NotAuthorizedException("Authorization error", "User access token not found")
    except:
        raise