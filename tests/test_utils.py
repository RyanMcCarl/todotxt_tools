#!/usr/bin/python3
# -*-coding: utf-8 -*-

import os
import pytest
import sys

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

#from timemap.todotxt_utils import check_for_files, check_for_paths, prefer_newer_files

# Likely todo.txt file locations


@pytest.fixture
def usual_paths():
    return ['~/todo', '~/Dropbox', '~/Dropbox/todo', '~/Dropbox/notes']


@pytest.fixture
def file_names():
    return ['todo.txt', 'someday.txt', 'done.txt']


@pytest.fixture
def check_for_files(file_names, valid_path_list):
    file_dict = {file: [] for file in file_names}
    for path in valid_path_list:
        assert os.path.exists(path) == True
        for file in file_names:
            path_plus_file = os.path.join(path, file)
            if os.path.isfile(path_plus_file):
                file_dict[file].append(path_plus_file)
    return file_dict


@pytest.fixture
def prefer_newer_files(file_dict):
    for file_name, file_path_list in file_dict.items():
        newest_file = max(file_path_list, key=os.path.getctime)
        file_dict[file_name] = newest_file
    return file_dict


def test_check_for_paths(usual_paths):
    valid_path_list = [path for path in usual_paths if os.path.exists(
        os.path.expanduser(path))]
    assert len(valid_path_list) == 4



# TODO - make cross-platform


def test_paths():
    paths = [lambda x: os.path.expanduser(x) for x in usual_paths()]
    print(paths)
    #assert os.path.expanduser('~/Dropbox/todo') in paths


