# import classes
from backend.database.Operations import *
from backend.common.Constants import *

noOfAppsPagesFacebook = numberOfFacebookAppPages() + 1
FacebookAppCount = NumberOfFacebookApps()

noOfAppsPagesTwitter = numberOfTwitterAppPages() + 1
TwitterAppCount = NumberOfTwitterApps()


def facebookAppStartIdAndEndId(facebookPageNum):
    global FacebookAppCount
    startId = FacebookAppCount - ((facebookPageNum - 1) * common.numOfAppsPerPage)
    if (startId - common.numOfAppsPerPage) > 0:
        endId = startId - common.numOfAppsPerPage
        return startId, endId
    else:
        endId = 1
        return startId, endId


def getFacebookAppList(startId, endId):
    list = []
    for i in range(endId, startId + 1):
        list.append(getFacebookAppDetailsById(i))
    return list

def twitterAppStartIdAndEndId(twitterPageNum):
    global TwitterAppCount
    startId = TwitterAppCount - ((twitterPageNum - 1) * common.numOfAppsPerPage)
    if (startId - common.numOfAppsPerPage) > 0:
        endId = startId - common.numOfAppsPerPage
        return startId, endId
    else:
        endId = 1
        return startId, endId


def getTwitterAppList(startId, endId):
    list = []
    for i in range(endId, startId + 1):
        list.append(getTwitterAppDetailsById(i))
    return list
