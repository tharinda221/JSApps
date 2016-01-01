from config import *

TOKENS = {}


class common:
    ApplicationSecret = ""


class facebook:
    secretKey = "810caf413c4786364eb65172fed5a03c"
    appID = "1672045909732059"
    GraphAPIVersion = "v2.5"
    redirectURL = "http://" + host + ":" + str(port) + "/callback"
    baseGraphApiUrl = "https://graph.facebook.com/v2.5/"
    getUserInitInfoUrl = "me?fields=name,birthday,about,bio,email,education,gender," \
                         "id,hometown"
