#!/usr/bin/env python3

import requests
import os


url = 'http://localhost/upload/'

path = 'supplier-data/images/'
files = os.listdir(path)
files = [file for file in files if file.endswith('jpeg')]

for file in files:
    with open(path + file, 'rb') as opened:
        r = requests.post(url, files={'file': opened}) 
