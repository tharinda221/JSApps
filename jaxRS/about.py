# import libraries
from flask_restful import Resource
from flask import make_response, render_template


class about(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('about/about.html'), 200, headers)
