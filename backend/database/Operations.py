# import libraries
import datetime
from bson.objectid import ObjectId
# import classes
from backend.plainObjects.user import *
from backend.plainObjects.apps import *
from backend.database.getDatabase import *
from backend.common.Constants import *


def putFacebookUserData(userId,
                        userName,
                        gender,
                        birthDay,
                        hometown,
                        email,
                        education,
                        about):
    databaseCollections.userFBCollectionName.insert_one(
            {
                "userId": userId,
                "userName": userName,
                "gender": gender,
                "birthday": birthDay,
                "hometown": hometown,
                "email": email,
                "education": education,
                "about": about
            }
    )
    print("Inserted facebookUser data")


def putTwitterUserData(userId,
                       userScreenName,
                       userName,
                       geoLocation,
                       country,
                       userDescription,
                       profileImage
                       ):
    databaseCollections.userTwitterCollectionName.insert_one(
            {
                "userId": userId,
                "userScreenName": userScreenName,
                "userName": userName,
                "geoLocation": geoLocation,
                "country": country,
                "userDescription": userDescription,
                "profileImage": profileImage
            }
    )
    print("Inserted twitterUser data")


def getFacebookUserAvailability(userId):
    if databaseCollections.userFBCollectionName.find({'userId': userId}).count() > 0:
        return False
    else:
        return True


def getTwitterUserAvailability(userScreenName):
    if databaseCollections.userTwitterCollectionName.find({'userScreenName': userScreenName}).count() > 0:
        return False
    else:
        return True


def putFacebookAppsData():
    databaseCollections.facebookAppsCollectionName.insert(
            {
                "AppName": "TestApp",
                "AppMethodName": "TestMethod",
                "AppImage": "images/appImages/app1/test.jpg",
                "AppSourceImage": "images/appImages/facebook/app1/testSource.jpg",
                "AppResultImage": "images/appImages/facebook/app1/testResult.jpg",
                "AppComments": [],
                "AppUsedCount": 0,
                "AppCreatedTime": datetime.datetime.utcnow()
            }
    )
    print("Inserted FacebookApps data")

def putTwitterAppsData():
    databaseCollections.twitterAppsCollectionName.insert(
            {
                "AppName": "TestApp",
                "AppMethodName": "TestMethod",
                "AppImage": "images/appImages/app1/test.jpg",
                "AppSourceImage": "images/appImages/twitter/app1/testSource.jpg",
                "AppResultImage": "images/appImages/twitter/app1/testResult.jpg",
                "AppComments": [],
                "AppUsedCount": 0,
                "AppCreatedTime": datetime.datetime.utcnow()
            }
    )
    print("Inserted TwitterApps data")

def rowCount(dbCollection):
    return dbCollection.count()


def NumberOfFacebookApps():
    return rowCount(databaseCollections.facebookAppsCollectionName)


def numberOfFacebookAppPages():
    total = NumberOfFacebookApps()
    if total % common.numOfAppsPerPage == 0:
        return (total - (total % common.numOfAppsPerPage)) / common.numOfAppsPerPage
    else:
        return (total - (total % common.numOfAppsPerPage)) / common.numOfAppsPerPage + 1


def getFacebookAppDetailsById(Id):
    document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(Id)})
    obj = facebookApps(appid=document["_id"],
                       appname=document["AppName"],
                       appmethodname=document["AppMethodName"],
                       appimage=document["AppImage"],
                       appresultimage=document["AppResultImage"],
                       appsourceimage=document["AppSourceImage"],
                       appcomments=document["AppComments"],
                       appusedcount=document["AppUsedCount"])
    return obj


def NumberOfTwitterApps():
    return rowCount(databaseCollections.twitterAppsCollectionName)


def numberOfTwitterAppPages():
    total = NumberOfTwitterApps()
    if total % common.numOfAppsPerPage == 0:
        return (total - (total % common.numOfAppsPerPage)) / common.numOfAppsPerPage
    else:
        return (total - (total % common.numOfAppsPerPage)) / common.numOfAppsPerPage + 1


def getTwitterAppDetailsById(Id):
    document = databaseCollections.twitterAppsCollectionName.find_one({'_id': ObjectId(Id)})

    obj = twitterApps(appid=document["_id"],
                      appname=document["AppName"],
                      appmethodname=document["AppMethodName"],
                      appimage=document["AppImage"],
                      appresultimage=document["AppResultImage"],
                      appsourceimage=document["AppSourceImage"],
                      appcomments=document["AppComments"],
                      appusedcount=document["AppUsedCount"])
    return obj


def getTwitterAppsIDList():
    return databaseCollections.twitterAppsCollectionName.distinct('_id')


def getFacebookAppsIDList():
    return databaseCollections.facebookAppsCollectionName.distinct('_id')
