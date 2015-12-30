from config import *

TOKENS = {}
USER = {"id": "", "name": ""}


class common:
    ApplicationSecret = ""


class facebook:
    secretKey = "810caf413c4786364eb65172fed5a03c"
    appID = "1672045909732059"
    GraphAPIVersion = "v2.5"
    redirectURL = "http://" + host + ":" + str(port) + "/callback"
    getUserID = "https://graph.facebook.com/me?access_token="
