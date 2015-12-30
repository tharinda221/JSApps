# import libraries
import dateutil.parser as parser

# import classes
from jaxRS.facebook import *


def togetherAllProfilePicsByYear():
    profileSourceArray = []
    profilePicsArray = getAlbumFromId(TOKENS["user_token"],
                                      getAlbumIdByName(TOKENS["user_token"], USER["id"], "Profile Pictures"))[
        "data"]
    for data in profilePicsArray:
        if parser.parse(data["created_time"]).year == 2015:
            profileSourceArray.append(data["source"])
    print(profileSourceArray)
