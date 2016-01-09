__author__ = 'tharinda'

# import classes
from jaxRS.facebook import *
from jaxRS.index import *
from jaxRS.facebookApps import *
from jaxRS.twitterApps import *
from jaxRS.twitter import *
# import libraries
import flask
from flask_restful import Api

app = flask.Flask(__name__)
api = Api(app)

api.add_resource(main, '/')
api.add_resource(authorizeFacebook, '/authorize/facebook')
api.add_resource(authorizeTwitter, '/authorize/twitter')
api.add_resource(handleCallbackFacebook, '/callback/facebook')
api.add_resource(handleCallbackTwitter, '/callback/twitter')
api.add_resource(getTwitterUserDetails, '/start/twitter')
api.add_resource(getPage, '/facebook/<int:pageNum>')
api.add_resource(getFacebookApp, '/facebook/appDetails/<int:appId>')
api.add_resource(runApplication, '/facebook/runApplication/<int:appId>')

