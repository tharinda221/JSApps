# import classes
from backend.database.Operations import *
from backend.common.Constants import *

noOfAppsPagesFacebook = numberOfFacebookAppPages() + 1
FacebookAppCount = NumberOfFacebookApps()


def facebookAppStartIdAndEndId(facebookPageNum):
    global FacebookAppCount
    startId = FacebookAppCount - ((facebookPageNum - 1) * common.numOfAppsPerPage)
    if (startId - common.numOfAppsPerPage) > 0:
        endId = startId - common.numOfAppsPerPage
        return startId, endId
    else:
        endId = 1
        return startId, endId


def getAppList(startId, endId):
    list = []
    for i in range(endId, startId + 1):
        list.append(getAppDetailsById(i))
    return list
