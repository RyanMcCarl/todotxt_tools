#!/usr/bin/python3
# -*-coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
        name="Timemap",
        description="Utilities for task and time management with todo.txt and .org files",
        version="0.1",
        packages=find_packages(),
        setup_requires=['pytest-runner'],
        tests_require=['pytest']

        )

