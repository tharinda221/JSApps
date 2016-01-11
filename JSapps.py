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

api.add_resource(main, '/', endpoint='/')
api.add_resource(facebook, '/facebook', endpoint='/facebook')
api.add_resource(twitter, '/twitter', endpoint='/twitter')
api.add_resource(authorizeFacebook, '/authorize/facebook')
api.add_resource(authorizeTwitter, '/authorize/twitter')
api.add_resource(handleCallbackFacebook, '/callback/facebook')
api.add_resource(handleCallbackTwitter, '/callback/twitter')
api.add_resource(getFacebookPage, '/facebook/<int:pageNum>')
api.add_resource(getFacebookApp, '/facebook/appDetails/<appId>')
api.add_resource(runFacebookApplication, '/facebook/runApplication/<appId>')
api.add_resource(getTwitterPage, '/twitter/<int:pageNum>')
api.add_resource(getTwitterApp, '/twitter/appDetails/<appId>')
api.add_resource(runTwitterApplicaions, '/twitter/runApplication/<appId>')
