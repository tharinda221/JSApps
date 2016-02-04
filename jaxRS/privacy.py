# import libraries
from flask_restful import Resource
from flask import make_response, render_template


class privacy(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('privacy/privacy.html'), 200, headers)
