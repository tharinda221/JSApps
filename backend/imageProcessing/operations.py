# import libraries
from PIL import Image, ImageSequence
from PIL import ImageFont
from PIL import ImageDraw
import requests
import numpy as np
from StringIO import StringIO
from backend.imageProcessing.imagesTogif import writeGif
# import classes
import config
import numpy


def writeTextToImage(text):
    BASE_DIR = config.BASE_DIR
    inputFilePath = BASE_DIR + "/JSApps/static/images/appImages/input.jpg"
    outputFilePath = BASE_DIR + "/JSApps/static/images/appImages/output.jpg"
    fontPath = BASE_DIR + "/JSApps/static/fonts/sans-serif.ttf"
    img = Image.open(inputFilePath)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(fontPath, 24)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0, 0), text, (0, 0, 0), font=font)
    img.save(outputFilePath)


def readImageFromURL(url):
    response = requests.get(url, verify=False)
    # img = np.array(Image.open(StringIO(response.content)))
    file = StringIO(response.content)
    img = Image.open(file)
    image = img.resize((150, 150), Image.ANTIALIAS)
    return image


def createGIF(images, filename):
    writeGif(filename, images, duration=0.5)


def findSoulMate(gender, age, skill):
    celebrity, celebURL = "", ""
    if gender == "male":
        if age < 35:
            if len(skill) < 5:
                celebrity = "Annalise Basso"
                celebURL = "http://ia.media-imdb.com/images/M/MV5BMTkwMDQzNjIxNl5BMl5BanBnXkFtZTgwMTQ4OTU2NDE@._V1_UY317_CR9,0,214,317_AL_.jpg"
            else:
                celebrity = "Scarlett Johansson"
                celebURL = "http://ia.media-imdb.com/images/M/MV5BMTUwNzMwMzgyOV5BMl5BanBnXkFtZTcwMjk0ODY1NA@@._V1._SX640_SY962_.jpg"
        else:
            celebrity = "Kate Walsh"
            celebURL = "http://ia.media-imdb.com/images/M/MV5BMTk2NDEzNzg3MV5BMl5BanBnXkFtZTcwNjI1Mzg2Mw@@._V1_UX214_CR0,0,214,317_AL_.jpg"
    else:
        if age < 35:
            celebrity = "George Clooney"
            celebURL = "http://ia.media-imdb.com/images/M/MV5BMjEyMTEyOTQ0MV5BMl5BanBnXkFtZTcwNzU3NTMzNw@@._V1_UY317_CR9,0,214,317_AL_.jpg"
        else:
            celebrity = "Sacha Baron Cohen"
            celebURL = "http://ia.media-imdb.com/images/M/MV5BMTkzMTY4Nzc2NF5BMl5BanBnXkFtZTgwODc3MDI2MDE@._V1_UY317_CR11,0,214,317_AL_.jpg"

    return celebrity, celebURL

def writeTextInImage(text,img,fontSize, x, y):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("static/fonts/sans-serif.ttf", fontSize)
    draw.text((x, y), text, (0, 0, 0), font=font)
    return img