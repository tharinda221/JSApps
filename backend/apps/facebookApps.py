# import libraries
import dateutil.parser as parser
# import classes
from jaxRS.facebook import *
from backend.imageProcessing.operations import *
from backend.plainObjects.user import *
import config


class facebookAppsMethods(object):
    def togetherAllProfilePicsByYear(self):
        profileSourceArray = []
        profilePicsArray = getAlbumFromId(TOKENS["user_token"],
                                          getAlbumIdByName(TOKENS["user_token"], User.userId, "Profile Pictures"))[
            "data"]
        for data in profilePicsArray:
            if parser.parse(data["created_time"]).year == 2015:
                profileSourceArray.append(data["source"])
        print(profileSourceArray)

    def PredictByBirthNumber(self):
        BASE_DIR = config.BASE_DIR
        DataPath = open(os.path.join(BASE_DIR, "JSApps/resources/", "appData.json"), "r")
        data = json.load(DataPath)["App1"]["data"][0]["prediction"]
        print("HERE")
        writeTextToImage(data)

    def TestMethod(self, appId):
        print("Method Accessed")
        profilePicsAlbumId = getAlbumIdByName(session["facebook_user_token"], session["facebookUser"]["userId"],
                                              "Profile Pictures")
        profilePicslist = getAlbumFromId(session["facebook_user_token"], profilePicsAlbumId)['data']
        profilePicsURLlist = []
        for profPics in profilePicslist:
            profilePicsURLlist.append(profPics['source'])
        images = []
        for profPicURL in profilePicsURLlist:
            images.append(readImageFromURL(profPicURL))
        createGIF(images=images, filename=config.AppsImagePath + "facebook/app1/result.gif")
        databaseCollections.facebookAppsCollectionName.update_one({'_id': ObjectId(appId)},
                                                                  {"$set": {
                                                                      "AppResultImage": "images/appImages/facebook/app1/result.gif"}}
                                                                  )

    # def profileImagesOnAGif(self):
    #     profilePicsURLlist = getAlbumIdByName(session["facebook_user_token"], session["facebookUser"]["userId"],
    #                                           "Profile Pictures")
    #     images = []
    #     for profPicURL in profilePicsURLlist:
    #         images.append(readImageFromURL(profPicURL))
    #     createAGIF(images=images, filename=config.AppsImagePath+"facebook/app1/result.gif")
