#! /usr/bin/env python3
import os
import requests

def list_directory(path):
    return [os.path.join('/data/feedback', file) for file in os.listdir(path)]
        
def parse_text(file):
    with open(file) as f:
        f_list = [line.strip() for line in f]
        return {'title':f_list[0], 'name':f_list[1], 'date':f_list[2], 'feedback':f_list[3]}

def request_post(data):
    return requests.post('http://35.188.49.216/feedback/', data=data)

def main():
    print(__name__)
    # files = list_directory('/data/feedback')
    # dict_list = []
    # for file in files:
    #     feedback_dict = parse_text(file)
    #     dict_list.append(feedback_dict)

    # for data in dict_list:
    #     print('Sending', data)
    #     request_post(data)
# if __name__ == "__main__":
#     main()

print(__name__)
