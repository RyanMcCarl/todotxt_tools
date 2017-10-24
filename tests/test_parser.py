#!/usr/env/python3
# -*-coding: utf-8 -*-

import os
import re
import sys
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

import pytest
from timemap.regexes import TaskRE

#@given(text())

#@pytest.fixture
# def regexes():
#    os.chdir()


@pytest.fixture
def broken_tasks():
    broken_task_list = [
    r"x (B) 2017-09-26 2017-10-10 2017-11-13 (A) Get front brakes replaced +errands",
    r"@2hours @5min due:2016-05-05 t:2017-09-09 due:2017-12-31 t:2018-09-10 rec:2m r:2w"]
    return broken_task_list

broken_task_1 = broken_tasks()[0]
broken_task_2 = broken_tasks()[1]


@pytest.fixture
def todotxt_file():
    with open('tests/todo.txt') as infile:
        return [l.strip() for l in infile.readlines()]


@pytest.fixture
def someday_file():
    with open('tests/someday.txt') as infile:
        return [l.strip() for l in infile.readlines()]


@pytest.fixture
def done_file():
    with open('tests/done.txt') as infile:
        return [l.strip() for l in infile.readlines()]


@pytest.fixture
def all_tasks():
    all_task_list = todotxt_file() + someday_file() + done_file()
    return all_task_list


@pytest.mark.parametrize("sample_tasks", [todotxt_file(), someday_file(), done_file()])
def test_parameterizing_correctly(sample_tasks):
    # Ensure we have a task list
    assert isinstance(sample_tasks, list)
    # Ensure there are at least 50 task lines read in from each file
    assert len(sample_tasks) >= 50


def test_all_tasks(all_tasks):
    assert isinstance(all_tasks, list)
    # Combined length of tasks should be over 400.
    assert len(all_tasks) > 400
    # Check to make sure we don't have nested lists.
    for l in all_tasks:
        assert isinstance(l, str)


@pytest.mark.parametrize("task", [t for t in all_tasks()])
def test_zero_or_one_priority_per_line(task):
    assert len(re.findall(TaskRE.priority, task)) < 2


def test_multiple_priorities_raises_error():
    with pytest.raises(AssertionError):
        assert len(re.findall(TaskRE.priority, broken_task_1)) < 2


@pytest.mark.parametrize("task", [t for t in all_tasks()])
def test_zero_or_one_due_date_per_line(task):
    assert len(re.findall(TaskRE.due_date, task)) < 2


def test_multiple_due_dates_raises_error():
    with pytest.raises(AssertionError):
        assert len(re.findall(TaskRE.due_date, broken_task_2)) < 2


@pytest.mark.parametrize("task", [t for t in all_tasks()])
def test_zero_or_one_threshold_date_per_line(task):
    assert len(re.findall(TaskRE.threshold_date, task)) < 2


def test_multiple_threshold_dates_raises_error():
    with pytest.raises(AssertionError):
        assert len(re.findall(TaskRE.threshold_date, broken_task_2)) < 2


@pytest.mark.parametrize("task", [t for t in all_tasks()])
def test_zero_or_one_creation_date_per_line(task):
    assert len(re.findall(TaskRE.creation_date, task)) < 2


@pytest.mark.parametrize("task", [t for t in all_tasks()])
def test_zero_or_one_effort_per_line(task):
    assert len(re.findall(TaskRE.effort, task)) < 2


def test_multiple_efforts_raises_error():
    with pytest.raises(AssertionError):
        assert len(re.findall(TaskRE.effort, broken_task_2)) < 2


@pytest.mark.parametrize("task", [t for t in all_tasks()])
def test_zero_or_one_completion_date_per_line(task):
    assert len(re.findall(TaskRE.completion_date, task)) < 2


def test_multiple_efforts_raises_error():
    with pytest.raises(AssertionError):
        assert len(re.findall(TaskRE.effort, broken_task_2)) < 2
