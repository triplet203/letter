from PIL import Image, ImageFont, ImageDraw

def draw ():

    img = Image.open('sample.jpg')
    title_font = ImageFont.truetype('Playfair_Display\PlayfairDisplay-VariableFont_wght.ttf',20)
    name = "The Beauty of Nature"
    msnv = '33815514'
    dep = 'MFO3'
    image_editable = ImageDraw.Draw(img)
    image_editable.text((20,750), name, (255, 255, 255), font=title_font)
    image_editable.text((20,800), msnv, (255, 255, 255), font=title_font)
    image_editable.text((105,800), dep, (255, 255, 255), font=title_font)
    img.save("result1.jpg")


draw()