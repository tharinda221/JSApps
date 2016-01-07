__author__ = 'tharinda'
# import classes
from backend.social.facebook import *
from backend.apps.facebookApps import *
# import libraries
from flask_restful import Resource

runApplicaions = facebookAppsMethods()


class appTogetherAllProfilePicsByYear(Resource):
    def get(self):
        method_name = 'PredictByBirthNumber'
        method = getattr(runApplicaions, method_name)
        if not method:
            raise Exception("Method %s not implemented" % method_name)
        method()
