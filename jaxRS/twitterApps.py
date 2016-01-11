__author__ = 'tharinda'
# import classes
from backend.social.twitter import *
from backend.database.Operations import *
# import libraries
from flask_restful import Resource


class getTwitterUserDetails(Resource):
    def get(self):
        return getTwitterUserDetails()