#!/usr/bin/python3

import argparse
import collections
import enum
from task import Task, CompletedTask, SomedayTask
from todotxt_utils import check_for_paths, check_for_files, prefer_newer_files, get_sorted_lines_from_file
import os
import pytest
import pprint
import sys
import re


pp = pprint.PrettyPrinter(indent=2)


def parse_args(args):
    parser = argparse.ArgumentParser(description='Clean up a todo.txt file.')
    parser.add_argument('file_path', help='the path to your todo.txt file', nargs='?') #metavar='str', type=str, nargs='?',
    return parser.parse_args(args)


def find_todotxt_files(file_path=None):
    path_list = [file_path] if file_path else ['~/todo', '~/Dropbox', '~/Dropbox/todo',
                                               '~/Dropbox/notes']
    valid_paths = check_for_paths([os.path.expanduser(path) for path in path_list])
    valid_files = check_for_files(['todo.txt', 'someday.txt', 'done.txt'], valid_paths)
    newest_file_dict = prefer_newer_files(valid_files)
    assert 'todo.txt' in newest_file_dict.keys(), "Couldn't find any todo.txt file!"
    assert 'done.txt' in newest_file_dict.keys(), "Couldn't find any done.txt file!"
    return newest_file_dict


def sort_and_dedupe_list(alist):
    return sorted({line for line in alist})


def make_task_dict(ttfdict):
    return {list_name: get_sorted_lines_from_file(ttfdict[list_name]) for list_name in ttfdict.keys()}


def main():
    args = parse_args(sys.argv[1:])
    todotxt_file_path = args.file_path
    todotxt_files_dict = find_todotxt_files(todotxt_file_path)
    task_dict = make_task_dict(todotxt_files_dict)
    try:
        pp.pprint(task_dict['todo.txt'][:10])
    except TypeError as e:
        print("Your task list seems to be empty. Are we discovering it correctly? {}".format(e))




if __name__ == '__main__':
    sys.exit(main())
