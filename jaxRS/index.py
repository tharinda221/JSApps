__author__ = 'tharinda'

from flask import Flask , make_response , render_template
from flask_restful import Resource
from backend.facebook import *

app = Flask(__name__)
class Main(Resource):

    def get(self):
        global TOKENS
        headers = {'Content-Type': 'text/html'}
        user_authorized = True if "user_token" in TOKENS else False
        return make_response(render_template('index.html', authorized=user_authorized),200,headers)