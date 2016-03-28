__author__ = 'tharinda'
# import classes
from restfulServices.facebook import *
from backend.plainObjects.user import *
from backend.database.Operations import *
from backend.frontEndOperaions.indexOperations import *
# import libraries
from flask import Flask, make_response, render_template, send_file
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove

# app = Flask(__name__)

class main(Resource):
    def get(self):
        return flask.redirect('/facebook')


class tempImage(Resource):
    def get(self, appId):
        tempFileObj = NamedTemporaryFile(mode='w+b', suffix='jpg')
        # pilImage = open('/home/tharinda/Working/projects/JSApps/static/images/appImages/facebook/app1/appImage.jpg',
        #                 'rb')
        pilImage = open(session["fileName"], 'rb')
        copyfileobj(pilImage, tempFileObj)
        pilImage.close()
        remove(session["fileName"])
        tempFileObj.seek(0, 0)
        response = send_file(tempFileObj, as_attachment=True, attachment_filename='image.jpg')
        return response
