#!/usr/bin/env python3
import os
import re
from PIL import Image

directory = os.listdir('module1_images')
try:
    os.mkdir('module1_images_processed')
except IOError:
    print('Directory already exists.')
for file in directory:
    im = Image.open('module1_images/' + file)
    filemod = re.search(r'([A-Za-z0-9\-\_]*)', file)
    im = im.resize((128, 128)).rotate(-90)
    im.save('module1_images_processed/' + filemod.group(1) + '.jpeg', 'jpeg')
    print(file)
