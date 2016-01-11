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

    def TestMethod(self):
        print("Method Accessed")
