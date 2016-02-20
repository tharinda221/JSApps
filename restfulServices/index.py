__author__ = 'tharinda'
# import classes
from restfulServices.facebook import *
from backend.plainObjects.user import *
from backend.database.Operations import *
from backend.frontEndOperaions.indexOperations import *
# import libraries
from flask import Flask, make_response, render_template


# app = Flask(__name__)

class main(Resource):
    def get(self):
        return flask.redirect('/facebook')
