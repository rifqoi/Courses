#! /usr/bin/env python3
import os
import requests
import re

def list_directory(path):
    return [os.path.join(path, file) for file in os.listdir(path)]
        
def parse_text(file):
    filename, ext = os.path.splitext(os.path.basename(file))
    with open(file) as f:
        f_list = [line.strip() for line in f]
        name = f_list[0]
        weight = int(re.search('(\d+)\s',f_list[1]).group(1))
        descriptions = f_list[2]
        image = filename+".jpeg"
        return {'name': name, 'weight': weight, 'description': descriptions, 'image_name': image}

def request_post(url, data):
    return requests.post(url, data=data)

files = list_directory('supplier-data/descriptions')
url = "http://34.67.255.248/fruits/"
dict_list = []
for file in files:
    feedback_dict = parse_text(file)
    dict_list.append(feedback_dict)

for data in dict_list:
    print('Sending', data)
    request_post(url, data)

