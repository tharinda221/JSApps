__author__ = 'tharinda'

import flask
from flask_restful import Api

from jaxRS.index import *
from backend.facebook import *
from jaxRS.facebook import *

app = flask.Flask(__name__)
api = Api(app)

api.add_resource(Main, '/')
api.add_resource(authorize_facebook, '/authorize')
api.add_resource(handle_callback, '/callback')
api.add_resource(user_details, '/userDetails')
#api.add_resource(facebook, '/social/<string:provider>', endpoint = 'social')

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)