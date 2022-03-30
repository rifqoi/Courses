#!/usr/bin/env python3
from PIL import Image
import os
import os

def resize_rotate(img):
    with Image.open(img).convert('RGB') as image:
        basename = os.path.basename(img)
        filename, _ = os.path.splitext(basename)
        image.rotate(-90).resize((128,128)).save("images_jpeg/" + filename + '.jpeg', "JPEG")

def main():
    for img in os.listdir('images'):
        img = 'images/' + img
        try:
            print('Editing ' + img)
            resize_rotate(img)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
