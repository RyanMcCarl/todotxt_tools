#!/usr/bin/python3

import os


def print_todotxt_file(filename):
    with open(filename) as infile:
        try:
            task_lines = [l.strip() for l in infile.readlines()][:10]
        except FileNotFoundError as e:
            print("We couldn't find your todo.txt file! {}".format(e))
        for l in task_lines:
            print(l)

def check_for_paths(path_list):
    valid_path_list = [path for path in path_list if os.path.exists(os.path.expanduser(path))]
    return valid_path_list

def check_for_files(file_names, valid_path_list):
    file_dict = {file:[] for file in file_names}
    for path in valid_path_list:
        assert os.path.exists(path) == True
        for file in file_names:
            path_plus_file = os.path.join(path, file)
            if os.path.isfile(path_plus_file):
                file_dict[file].append(path_plus_file)
    return file_dict

def prefer_newer_files(file_dict):
    for file_name, file_path_list in file_dict.items():
        newest_file = max(file_path_list, key=os.path.getctime)
        file_dict[file_name] = newest_file
    return file_dict


def get_sorted_lines_from_file(file_path):
    pass

if __name__ == '__main__':
    print("Do not run this module directly.")
    pass
