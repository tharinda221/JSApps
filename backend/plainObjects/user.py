class User:
    def __init__(self):
        pass

    class facebook:
        def __init__(self):
            pass

        userId = ""
        userName = ""
        gender = ""
        birthDay = ""
        hometown = ""
        email = ""
        education = []
        about = ""
        country = ""

    class twitterUser(object):
        def __init__(self, userId="",
                     userScreenName="",
                     userName="",
                     geoLocation="",
                     country="",
                     userDescription="",
                     profileImage=""
                     ):
            self.userDescription = userDescription
            self.profileImage = profileImage
            self.geoLocation = geoLocation
            self.country = country
            self.userName = userName
            self.userScreenName = userScreenName
            self.userId = userId
