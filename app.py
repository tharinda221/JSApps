__author__ = 'tharinda'


from jaxRS.index import *
import flask
from flask_restful import Api



app = flask.Flask(__name__)
api = Api(app)


api.add_resource(Main, '/')



if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)