#!/usr/bin/env python3

import sys
import subprocess

file = sys.argv[1]

# with open(file) as f:
#     file_list = [filename.strip() for filename in f.readlines()]
#     new_file_list = [filename.replace('jane', 'jdoe').strip() for filename in file_list]
#     for old, new in zip(file_list, new_file_list):
#         subprocess.run(['mv', old, new])

with open(file) as f:
    for file in f:
        file = file.strip()
        new_file = file.replace('jane', 'jdoe')
        subprocess.run(['mv', file, new_file])

# print(file_list)

