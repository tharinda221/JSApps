# import libraries
import datetime

# import classes
from backend.plainObjects.user import *
from backend.plainObjects.apps import *
from backend.database.getDatabase import *
from backend.common.Constants import *


def putFacebookUserData():
    result = databaseCollections.userFBCollectionName.insert_one(
            {
                "userId": User.facebook.userId,
                "userName": User.facebook.userName,
                "gender": User.facebook.gender,
                "birthday": User.facebook.birthDay,
                "hometown": User.facebook.hometown,
                "email": User.facebook.email,
                "education": User.facebook.education,
                "about": User.facebook.about
            }
    )
    print(result.inserted_id)


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
    print("Inserted tiwtterUser data")


def getTwitterUserAvailability(userScreenName):
    if databaseCollections.userTwitterCollectionName.find({'userScreenName': userScreenName }).count() > 0:
        return False
    else:
        return True


def putFacebookAppsData():
    databaseCollections.facebookAppsCollectionName.insert(
            {
                "AppID": 1,
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
    print("Inserted")


def putTwitterAppsData():
    databaseCollections.twitterAppsCollectionName.insert(
            {
                "AppID": 1,
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
    print("Inserted")


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
    document = databaseCollections.facebookAppsCollectionName.find({"AppID": Id})
    obj = facebookApps(appid=document[0]["AppID"],
                       appname=document[0]["AppName"],
                       appmethodname=document[0]["AppMethodName"],
                       appimage=document[0]["AppImage"],
                       appresultimage=document[0]["AppResultImage"],
                       appsourceimage=document[0]["AppSourceImage"],
                       appcomments=document[0]["AppComments"],
                       appusedcount=document[0]["AppUsedCount"])
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
    document = databaseCollections.twitterAppsCollectionName.find({"AppID": Id})
    obj = twitterApps(appid=document[0]["AppID"],
                      appname=document[0]["AppName"],
                      appmethodname=document[0]["AppMethodName"],
                      appimage=document[0]["AppImage"],
                      appresultimage=document[0]["AppResultImage"],
                      appsourceimage=document[0]["AppSourceImage"],
                      appcomments=document[0]["AppComments"],
                      appusedcount=document[0]["AppUsedCount"])
    return obj
