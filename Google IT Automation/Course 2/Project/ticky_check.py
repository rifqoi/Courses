import os
import csv
import operator
from collections import OrderedDict
import re

def generate_error(syslog):
    error_regex = re.compile(r"ERROR ([\w\s\']+)")
    error_list = []
    with open(syslog) as file:    
        file = file.readlines()
        for error in file:
            error_match = error_regex.findall(error)
            if error_match:
                error_list.append(error_match)
    error_list = [', '.join(error).strip() for error in error_list]
    # error_list = [error.strip() for error in error_list]
    print(error_list)

    error_dict = {}
    for key in error_list:
        error_dict[key] = error_dict.get(key, 0)
        error_dict[key] += 1

    error_dict = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
    # error_dict = OrderedDict(error_dict)
    return error_dict

def user_info_error(syslog):
    user_regex = re.compile(r"\(([\w\.]+)\)")
    
    with open(syslog) as file:
        file_list = file.readlines()
        info_list = []
        error_list = []
        info_dict = {}
        error_dict = {}
        for string in file_list:
            if "INFO" in string:
                info_list.append(string.strip())
            if "ERROR" in string:
                error_list.append(string.strip())

        error_list = [user_regex.search(user).group(1) for user in error_list]
        info_list = [user_regex.search(user).group(1) for user in info_list]

        for info, error in zip(info_list, error_list):
            info_dict[info] = info_dict.get(info, info_list.count(info))
            error_dict[error] = error_dict.get(error, error_list.count(error))
        
        # info_dict = sorted(info_dict.items())
        # error_dict = sorted(error_dict.items())

        total_dict = []
        for key_error, value_error  in error_dict.items():
            key_info = info_dict.get(key_error, 0)
            total_dict.append((key_error, key_info, value_error))
                
        return sorted(total_dict)

def dict_to_csv(dictionary, csv_filename, keys):   
    with open(csv_filename, 'w') as file:
        writer= csv.writer(file)
        writer.writerow(keys)
        writer.writerows(dictionary)
    

user_log =user_info_error(os.path.expanduser('~/syslog.log'))
dict_to_csv(user_log, os.path.expanduser('~/users_statistics.csv'), ['Username', 'Info', 'Error'])
