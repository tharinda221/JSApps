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
    image = img.resize((720, 720), Image.ANTIALIAS)
    return image


def createGIF(images, filename):
    writeGif(filename, images, duration=0.5)
