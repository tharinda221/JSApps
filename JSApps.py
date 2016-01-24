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

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

api.add_resource(main, '/', endpoint='/')
api.add_resource(facebook, '/facebook', endpoint='/facebook')
api.add_resource(twitter, '/twitter', endpoint='/twitter')
# api.add_resource(authorizeFacebook, '/authorize/facebook', endpoint='/authorize/facebook')
# api.add_resource(handleCallbackFacebook, '/callback/facebook', endpoint='/callback/facebook')
api.add_resource(authorizeTwitter, '/authorize/twitter', endpoint='/authorize/twitter')
api.add_resource(handleCallbackTwitter, '/callback/twitter', endpoint='/callback/twitter')
api.add_resource(getFacebookPage, '/facebook/<int:pageNum>', endpoint='/facebook/<int:pageNum>')
api.add_resource(getFacebookApp, '/facebook/appDetails/<appId>', endpoint='/facebook/appDetails/<appId>')
api.add_resource(runFacebookApplication, '/facebook/runApplication/<appId>',
                 endpoint='/facebook/runApplication/<appId>')
api.add_resource(getTwitterPage, '/twitter/<int:pageNum>', endpoint='/twitter/<int:pageNum>')
api.add_resource(getTwitterApp, '/twitter/appDetails/<appId>', endpoint='/twitter/appDetails/<appId>')
api.add_resource(runTwitterApplicaions, '/twitter/runApplication/<appId>', endpoint='/twitter/runApplication/<appId>')

api.add_resource(facebookLogin, '/authorize/facebook', endpoint='/authorize/facebook')
api.add_resource(facebookAuthorized, '/callback/facebook')
