class Apps(object):
    def __init__(self, appid = "",
                 appname = "",
                 appmethodname = "",
                 appimage = "",
                 appsourceimage = "",
                 appresultimage = "",
                 appsocialname = "",
                 appcomments = [],
                 appusedcount = "",
                 appcreatedtimedate = "",
                 appdescription = ""
                 ):
        self.AppDescription = appdescription
        self.AppCreatedTimeDate = appcreatedtimedate
        self.AppUsedCount = appusedcount
        self.AppComments = appcomments
        self.AppSocialName = appsocialname
        self.AppResultImage = appresultimage
        self.AppSourceImage = appsourceimage
        self.AppImage = appimage
        self.AppMethodName = appmethodname
        self.AppName = appname
        self.AppID = appid