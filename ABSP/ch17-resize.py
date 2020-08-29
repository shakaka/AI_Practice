# resize and add logo

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

#loop all files in the working directory
os.makedirs('withLogo',exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')\
            or filename == LOGO_FILENAME):
            im = Image.open(filename)
            width, height = im.size

            # check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE/width)*height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height)*width)
            height = SQUARE_FIT_SIZE
        # resize the image
        print('resizing %s...' %(filename))
        im = im.resize((width,height))

        # add the logo
        print('adding logo to %s ' %(filename))
        im.paste(logoIm, (width-logoWidth,height-logoHeight), logoIm)

        # save image
        im.save(os.path.join('withlogo', filename))
