__author__ = 'tharinda'
# import classes
from backend.social.facebook import *
from backend.apps.Apps import *
# import libraries
from flask_restful import Resource

class appTogetherAllProfilePicsByYear(Resource):
    def get(self):
        togetherAllProfilePicsByYear()