#!/usr/bin/python3
# -*-coding: utf-8 -*-

import sys

class MultipleFieldsException(BaseException):
    def __init__(self, taskline='', field_name='', field_occurrences=[]):
        msg = """This task line has too many occurrences of the {field_name} field.
        
        Task line: {taskline}\n\n
        Field name: {field_name}\n\n
        Field values found: {field_occurrences}\n\n
        """.format(field_name=field_name, taskline=taskline, field_occurrences=field_occurrences)
        BaseException.__init__(self, msg)

