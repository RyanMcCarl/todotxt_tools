#!/usr/bin/python3

import argparse
import collections
from todotxt_utils import check_for_paths, check_for_files, prefer_newer_files
import os
import pytest
import sys

def _parse_args(args):
    parser = argparse.ArgumentParser(description='Clean up a todo.txt file.')
    parser.add_argument('file_path', help='the path to your todo.txt file', nargs='?') #metavar='str', type=str, nargs='?',
    return parser.parse_args(args)

def print_todotxt_file(filename):
    with open(filename) as infile:
        _task_lines = [l.strip() for l in infile.readlines()][:10]
        for l in _task_lines:
            print(l)

def find_todotxt_files(file_path=None):
    _path_list = [file_path] if file_path else ['~/todo', '~/Dropbox', '~/Dropbox/todo', '~/Dropbox/notes']
    _valid_paths = check_for_paths([os.path.expanduser(path) for path in _path_list])
    _valid_files = check_for_files(['todo.txt', 'someday.txt', 'done.txt'], _valid_paths)
    _newest_file_dict = prefer_newer_files(_valid_files)
    assert 'todo.txt' in _newest_file_dict.keys(), "Couldn't find any todo.txt file!"
    assert 'done.txt' in _newest_file_dict.keys(), "Couldn't find any done.txt file!"
    return _newest_file_dict

def main():
    args = _parse_args(sys.argv[1:])
    todotxt_file_path = args.file_path
    todotxt_files = find_todotxt_files(todotxt_file_path)
    #print(todotxt_files)
    print_todotxt_file(todotxt_files['todo.txt'])


if __name__ == '__main__':
    sys.exit(main())
