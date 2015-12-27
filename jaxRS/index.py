__author__ = 'tharinda'

import flask
from flask_restful import Resource, Api

app = flask.Flask(__name__)
api = Api(app)

class Main(Resource):
    def get(self):
        return {'status': 'success'}