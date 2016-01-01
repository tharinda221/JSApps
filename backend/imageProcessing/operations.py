# import libraries
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# import classes
import config


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
