__author__ = 'tharinda'

# import classes
from jaxRS.facebook import *
from jaxRS.index import *
from config import *
# import libraries
import flask
from flask_restful import Api

app = flask.Flask(__name__)
api = Api(app)

api.add_resource(Main, '/')
api.add_resource(authorize_facebook, '/authorize')
api.add_resource(handle_callback, '/callback')

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
