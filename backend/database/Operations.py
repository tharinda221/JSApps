# import libraries
from __future__ import print_function
import boto3
import json
import decimal

# import classes
from backend.plainObjects.user import *
from backend.plainObjects.apps import *
from backend.database.connection import *
import config

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def putUserData():
    connection = getConnection()

    table = connection.Table('Users')

    userId = User.userId
    userName = User.userName
    gender = User.gender
    birthDay = User.birthDay
    hometown = User.hometown
    email = User.email
    education = User.education
    about = User.about

    response = table.put_item(
            Item={
                'userId': userId,
                'userName': userName,
                'gender': gender,
                'birthDay': birthDay,
                'hometown': hometown,
                'email': email,
                'education': education,
                'about': about,
            }
    )

    print("PutItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))
def putAppsData():
    connection = getConnection()

    table = connection.Table('Apps')

    # AppID = Apps.AppID
    # AppName = Apps.AppName
    # AppMethodName = Apps.AppMethodName
    # AppImage = Apps.AppImage
    # AppSourceImage = Apps.AppSourceImage
    # AppResultImage = Apps.AppResultImage
    # AppSocialName = Apps.AppSocialName
    # AppComments = Apps.AppComments
    # AppUsedCount = Apps.AppUsedCount
    # AppCreatedTimeDate = Apps.AppCreatedTimeDate
    AppID = "1"
    AppName = "Image show"
    AppMethodName = "ImageShow"
    AppImage = config.AppsImagePath + "App1/app1.jpg"
    AppSourceImage = config.AppsImagePath + "App1/App1In.jpg"
    AppResultImage = config.AppsImagePath + "App1/App1Out.jpg"
    AppSocialName = "facebook"
    AppComments = []
    AppUsedCount = 0
    AppCreatedTimeDate = "2016.1.1"

    response = table.put_item(
            Item={
                'AppID': AppID,
                'AppCreatedTimeDate': AppCreatedTimeDate,
                'AppMethodName': AppMethodName,
                'AppImage': AppImage,
                'AppSourceImage': AppSourceImage,
                'AppResultImage': AppResultImage,
                'AppSocialName': AppSocialName,
                'AppComments': AppComments,
                'AppUsedCount': AppUsedCount,
                'AppName': AppName
            }
    )
    print("PutItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))
