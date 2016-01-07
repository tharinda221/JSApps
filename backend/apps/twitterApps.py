# import classes
from backend.social.twitter import *

def printUserInfo():
    resp = getUserDetails()
    print(resp)