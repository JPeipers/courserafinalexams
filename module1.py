#!/usr/bin/env python3
import os
import re
from PIL import Image
# Lists all files in the 'module1_images' directory
directory = os.listdir('module1_images')
# Tries to make result directory
try:
    os.mkdir('module1_images_processed')
except IOError:
    print('Directory already exists.')

for file in directory:
    im = Image.open('module1_images/' + file)
    filemod = re.search(r'([A-Za-z0-9\-\_]*)', file)
    # Converts image to 'RGB' for JPEG, resizes, rotates and saves the result as JPEG
    im.convert('RGB').resize((128, 128)).rotate(-90).save('module1_images_processed/' + filemod.group(1) + '.jpeg', 'jpeg')
    print(file)
