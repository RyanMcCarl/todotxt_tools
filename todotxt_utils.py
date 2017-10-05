#!/usr/bin/python3

import os

def check_for_paths(_path_list):
    _valid_path_list = [path for path in _path_list if os.path.exists(path)]
    return _valid_path_list

def check_for_files(_file_names, _valid_path_list):
    _file_dict = {file:[] for file in _file_names}
    for _path in _valid_path_list:
        assert os.path.exists(_path) == True
        for _file in _file_names:
            _path_plus_file = os.path.join(_path, _file)
            if os.path.isfile(_path_plus_file):
                _file_dict[_file].append(_path_plus_file)
    return _file_dict

def prefer_newer_files(_file_dict):
    for _file_name, _file_path_list in _file_dict.items():
        _newest_file = max(_file_path_list, key=os.path.getctime)
        _file_dict[_file_name] = _newest_file
    return _file_dict

if __name__ == '__main__':
    print("Do not run this module directly.")
    pass
