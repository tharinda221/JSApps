# import libraries
import datetime

# import classes
from backend.plainObjects.user import *
from backend.plainObjects.apps import *
from backend.database.getDatabase import *
from backend.common.Constants import *


def putFacebookUserData():
    result = databaseOperations.userFBCollectionName.insert_one(
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


def putTwitterUserData():
    result = databaseOperations.userFBCollectionName.insert_one(
            {
                "userId": User.twitter.userId,
                "userScreenName": User.twitter.userScreenName,
                "userName": User.twitter.userName,
                "gender": User.twitter.gender,
                "birthday": User.twitter.birthday,
                "bio": User.twitter.bio,
                "email": User.twitter.email,
                "phoneNumber": User.twitter.phoneNumber

            }
    )
    print(result.inserted_id)


def putFacebookAppsData(id):
    databaseOperations.facebookAppsCollectionName.insert(
            {
                "AppID": id,
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
    databaseOperations.twitterAppsCollectionName.insert(
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

def numberOfFacebookAppPages():
    total = rowCount(databaseOperations.facebookAppsCollectionName)
    if( total % 6 == 0):
        return (total - ( total % 6) ) / 6
    else:
        return (total - ( total % 6) ) / 6 +1