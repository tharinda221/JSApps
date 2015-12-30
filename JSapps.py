__author__ = 'tharinda'

# import classes
from jaxRS.facebook import *
from jaxRS.index import *
from jaxRS.Apps import *

# import libraries
import flask
from flask_restful import Api

app = flask.Flask(__name__)
api = Api(app)

api.add_resource(main, '/')
api.add_resource(appDetails, '/appDetails')
api.add_resource(authorizeFacebook, '/authorize')
api.add_resource(handleCallback, '/callback')
api.add_resource(appTogetherAllProfilePicsByYear, '/start')

