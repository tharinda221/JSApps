__author__ = 'tharinda'

# import classes
from jaxRS.facebook import *
from jaxRS.index import *
from jaxRS.facebookApps import *
from jaxRS.twitterApps import *
from jaxRS.twitter import *
from jaxRS.about import *
from jaxRS.privacy import *
# import libraries
import flask
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)
app.secret_key = os.urandom(24)

api.add_resource(main, '/', endpoint='/')
api.add_resource(facebook, '/facebook', endpoint='/facebook')
api.add_resource(twitter, '/twitter', endpoint='/twitter')
api.add_resource(facebookLogin, '/authorize/facebook', endpoint='/authorize/facebook')
api.add_resource(facebookAuthorized, '/callback/facebook')
api.add_resource(authorizeTwitter, '/authorize/twitter', endpoint='/authorize/twitter')
api.add_resource(handleCallbackTwitter, '/callback/twitter', endpoint='/callback/twitter')
api.add_resource(getFacebookPage, '/facebook/<int:pageNum>', endpoint='/facebook/')
api.add_resource(getFacebookApp, '/facebook/appDetails/<appId>', endpoint='/facebook/appDetails/appId')
api.add_resource(getFacebookUserCreatableApps, '/facebook/UserCreatableAppsDetails/<appId>/<int:pageNum>')
api.add_resource(runFacebookApplication, '/facebook/runApplication/<appId>',
                 endpoint='/facebook/runApplication/<appId>')
api.add_resource(getTwitterPage, '/twitter/<int:pageNum>', endpoint='/twitter/')
api.add_resource(getTwitterApp, '/twitter/appDetails/<appId>', endpoint='/twitter/appDetails/')
api.add_resource(runTwitterApplicaions, '/twitter/runApplication/<appId>', endpoint='/twitter/runApplication/')
api.add_resource(shareFacebookResults, '/facebook/share/<appId>', endpoint='/facebook/share')
api.add_resource(shareTwitterResults, '/twitter/share/<appId>', endpoint='/twitter/share')
api.add_resource(about, '/about', endpoint='/about')
api.add_resource(privacy, '/privacy', endpoint='/privacy')

