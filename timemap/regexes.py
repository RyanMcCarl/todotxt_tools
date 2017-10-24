#!/usr/bin/python3
# -*-coding: utf-8 -*-

import re

class Objectview(object):
    def __init__(self, d):
        self.__dict__ = d

task_regexes = {"taskline": re.compile(r'^.*\w+.*$'),
                "task": re.compile(r'\([A-Z]\)|\d{4}\-\d{2}\-\d{2}|due:|t:|\+\w+|@[\w\d]+|[r|rec]:\d+\w+'),
                "completed": re.compile(r'^(?P<COMPLETED>\s?x\s)'),
                "priority": re.compile(r'\(([A-Z])\)'),
                "someday": re.compile(r'@\b(?P<SOMEDAY>someday)\b'),
                "tags": re.compile(r'(?<=\+)(?P<TAG>\w+)'),
                "taskline": re.compile(r'^(.*)$'),

                # If the context starts with a number, it is treated as effort
                "contexts": re.compile(r'@\b(?P<CONTEXT>\D+)\b'),
                "effort": re.compile(r'(?<=@)(?P<NUMBER>\d+)(?P<UNITS>(?P<MINUTES>min)|(?P<HOURS>hours))'),

                # Dates
                "creation_date": re.compile(r'(?<!due:)(?<!t:)(?<!-\d\d )(?P<CREATIONDATE>\b\d{4}-\d{2}-\d{2}\b)'),
                "threshold_date": re.compile(r'(?<=t:)(?P<THRESHOLDDATE>\d{4}-\d{2}-\d{2})'),
                "due_date": re.compile(r'(?<=due:)(?P<DUEDATE>\d{4}-\d{2}-\d{2})'),
                "completion_date": re.compile(r'(?<!due:)(?<!t:)(?<=-\d\d )(?P<CREATIONDATE>\b\d{4}-\d{2}-\d{2}\b)'),
                "iso_date": re.compile(r'(\b\d{4}-\d{2}-\d{2}\b)'),
                "bad_date": re.compile(r'\b(\d{1,2}/\d{1,2}/\d{1,2}\b)')}


TaskRE = Objectview(task_regexes)

def main():
    print(TaskRE.isodate)
    print(type(TaskRE.isodate))
if __name__ == '__main__':
    main()