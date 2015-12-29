from config import *

TOKENS = {}
USER = {"id": "", "name": ""}


class common:
    ApplicationSecret = ""


class facebook:
    secretKey = "cb5fcc9d29666ecb06ef35f9bdeddc54"
    appID = "1061202120578874"
    GraphAPIVersion = "v2.4"
    redirectURL = "http://" + host + ":" + str(port) + "/callback"
    getUserID = "https://graph.facebook.com/me?access_token="
