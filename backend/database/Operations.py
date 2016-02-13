# import libraries
import datetime
from bson.objectid import ObjectId
# import classes
from backend.plainObjects.user import *
from backend.plainObjects.apps import *
from backend.database.getDatabase import *
from backend.common.Constants import *
import math


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
                "AppName": "Profile Pic creator",
                "AppMethodName": "TestMethod",
                "AppImage": "images/appImages/facebook/app1/appImage.jpg",
                "AppSourceImage": "images/appImages/facebook/app1/background.jpg",
                "AppResultImage": "images/appImages/facebook/app1/appResultImage.jpg",
                "AppUsedCount": 0,
                "AppCreatedTime": datetime.datetime.utcnow(),
                "AppDescription": "Use this for your memorable occasion",
                "AppType": "userCreatable"
            }
    )
    print("Inserted FacebookApp data")


def FacebookUserCreatableAppsData():
    databaseCollections.facebookUserCreatableAppsCollectionName.insert(
            {
                "AppName": "Profile Pic creator",
                "AppMethodName": "TestMethod",
                "AppImage": "images/appImages/facebook/app1/appImage.jpg",
                "AppSourceImage": "images/appImages/facebook/app1/background.jpg",
                "AppFilteringImage": "images/appImages/facebook/app1/appResultImage.jpg",
                "AppUsedCount": 0,
                "AppCreatedTime": datetime.datetime.utcnow(),
                "AppDescription": "Use this for your memorable occasion",
                "AppMessage": "Change your profile picture against CEPA/ETCA",
                "AppPerentId": "56bf6355380dab5a65b7935b"
            }
    )
    print("Inserted FacebookUserCreatableApp data")


def putTwitterAppsData():
    databaseCollections.twitterAppsCollectionName.insert(
            {
                "AppName": "Your Most Used Words",
                "AppMethodName": "TestMethod",
                "AppImage": "images/appImages/twitter/app1/appImage.jpg",
                "AppSourceImage": "images/appImages/twitter/app1/background.jpg",
                "AppResultImage": "images/appImages/twitter/app1/appResultImage.jpg",
                "AppUsedCount": 0,
                "AppCreatedTime": datetime.datetime.utcnow(),
                "AppDescription": "This app will read your tweets and out you mostly used words in twitter",
                "AppMessage": "This app will read your tweets and out you mostly used words in twitter"
            }
    )
    print("Inserted TwitterApps data")


def rowCount(dbCollection):
    return dbCollection.count()


def NumberOfFacebookApps():
    return rowCount(databaseCollections.facebookAppsCollectionName)


def NumberOfFacebookUserCreatableApps():
    return rowCount(databaseCollections.facebookUserCreatableAppsCollectionName)


def numberOfFacebookAppPages():
    total = NumberOfFacebookApps()
    return math.ceil(total / common.numOfAppsPerPage)

def numberOfUserCreatableFacebookAppPages():
    total = NumberOfFacebookUserCreatableApps()
    return math.ceil(total / common.numOfAppsPerPage)

def getFacebookAppDetailsById(Id):
    document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(Id)})
    obj = facebookApps(appid=document["_id"],
                       appname=document["AppName"],
                       appmethodname=document["AppMethodName"],
                       appimage=document["AppImage"],
                       appresultimage=document["AppResultImage"],
                       appsourceimage=document["AppSourceImage"],
                       appusedcount=document["AppUsedCount"],
                       appdescription=document["AppDescription"],
                       apptype=document["AppType"])

    return obj

def getFacebookUserCreatableAppDetailsById(Id):
    document = databaseCollections.facebookUserCreatableAppsCollectionName.find_one({'_id': ObjectId(Id)})
    obj = facebookUserCreatable(appid=document["_id"],
                       appname=document["AppName"],
                       appmethodname=document["AppMethodName"],
                       appimage=document["AppImage"],
                       appfilteringimage=document["AppFilteringImage"],
                       appsourceimage=document["AppSourceImage"],
                       appusedcount=document["AppUsedCount"],
                       appdescription=document["AppDescription"],
                       appmessage=document["AppMessage"],
                       appparentid=document["AppParentId"]
    )
    return obj

def NumberOfTwitterApps():
    return rowCount(databaseCollections.twitterAppsCollectionName)


def numberOfTwitterAppPages():
    total = NumberOfTwitterApps()
    return math.ceil(total / common.numOfAppsPerPage)


def getTwitterAppDetailsById(Id):
    document = databaseCollections.twitterAppsCollectionName.find_one({'_id': ObjectId(Id)})

    obj = twitterApps(appid=document["_id"],
                      appname=document["AppName"],
                      appmethodname=document["AppMethodName"],
                      appimage=document["AppImage"],
                      appresultimage=document["AppResultImage"],
                      appsourceimage=document["AppSourceImage"],
                      appusedcount=document["AppUsedCount"],
                      appdescription=document["AppDescription"])
    return obj


def getTwitterAppsIDList():
    return databaseCollections.twitterAppsCollectionName.distinct('_id')


def getFacebookAppsIDList():
    return databaseCollections.facebookAppsCollectionName.distinct('_id')


def getFacebookUserCreatableAppsIDList(parentAppId):
    list = []
    for data in  databaseCollections.facebookUserCreatableAppsCollectionName.find({"AppPerentId": parentAppId}):
        list.append(data["_id"])
    return list
# def increaseAppCount(dbCollection):