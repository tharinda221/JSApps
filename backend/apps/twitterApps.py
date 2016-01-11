# import classes
from backend.social.twitter import *

def printUserInfo():
    resp = getTwitterUserDetails()
    print(resp)