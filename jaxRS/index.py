__author__ = 'tharinda'
# import classes
from jaxRS.facebook import *
# import libraries
from flask import Flask, make_response, render_template

app = Flask(__name__)


class main(Resource):
    def get(self):
        global TOKENS
        global USER
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(render_template('index.html', authorized=userAuthorized, id=USER["id"],
                                             name=USER["name"]), 200, headers)


class appDetails(Resource):
    def get(self):
        global TOKENS
        global USER
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "user_token" in TOKENS else False
        return make_response(render_template('AppDetails.html', authorized=userAuthorized, id=USER["id"],
                                             name=USER["name"]), 200, headers)
