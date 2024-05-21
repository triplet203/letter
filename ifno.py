import pandas as pd
import os
import pandas as pd
import openpyxl
from openpyxl import Workbook, load_workbook
from PIL import Image, ImageFont, ImageDraw, ImageOps

im=Image.open("sample.jpg")



def namero ():
    for i in name:
    width, height = 700,100
    font =  ImageFont.truetype('Playfair_Display\PlayfairDisplay-Italic-VariableFont_wght.ttf',60)
    image2 = Image.new('RGBA', (width, height), (255, 255, 255, 1))
    draw2 = ImageDraw.Draw(image2)
    draw2.text((0, 0), text='Dao Nguyen Nhat Huynh', font=font, fill=(0, 0, 0))
    image2 = image2.rotate(270, expand=1)
    px, py = 2250, 100
    sx, sy = image2.size
    im.paste(image2, (px, py, px + sx, py + sy), image2)
    im.show()
    im.save("result1.jpg")