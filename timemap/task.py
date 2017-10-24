import enum
import re
import pprint as pp
import os
import sys
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))
from timemap.regexes import TaskRE


#pp = pprint.PrettyPrinter(indent=2)

class TaskConfig(object):
    default_priority = 'B'
    lowest_priority = 'C'


class Task(object):

    def __init__(self, taskline, priority='B', completed=False, creation_date=None, threshold_date=None,
                 due_date=None, effort=None, tags=[], contexts=[], **kwargs):

        self.taskline = str(taskline)
        self.priority = priority
        self.completed = completed
        self.creation_date = creation_date
        self.threshold_date = threshold_date
        self.due_date = due_date
        self.effort = effort
        self.tags = tags
        self.contexts = contexts

        if kwargs:
            for k, v in kwargs.items():
                self.__setattr__(k, v)

        self.task = Task.parse_task(self)
        self.completed = Task.is_completed(self)
        self.effort = Task.parse_effort(self)
        Task.process_single_value_attributes(self)
        Task.process_multi_value_attributes(self)

    def __str__(self):
        taskline = self.taskline.strip()
        return taskline

    def __repr__(self):
        return "{0}".format(pp.pprint(self.taskline))

    def is_completed(self):
        completedRE = TaskRE.completed
        if completedRE.search(self.taskline):
            self.completed = True
            return True
        else:
            self.completed = False
            return False

    def parse_effort(self):
        if not re.search(TaskRE.effort, self.taskline):
            self.effort = None
            return None
        num = int(re.search(TaskRE.effort, self.taskline).group('NUMBER'))
        hours = re.search(TaskRE.effort, self.taskline).group('HOURS')
        if hours:
            effort, self.effort = num * 60, num * 60
            return effort
        else:
            effort, self.effort = num, num
            return effort



    def process_single_value_attributes(self):
        single_value_attribs = ['priority', 'creation_date', 'threshold_date', 'due_date']
        for attrib in single_value_attribs:
            attribRE = eval(r"TaskRE.{}".format(attrib))
            if re.search(attribRE, self.taskline):
                value = re.findall(attribRE, self.taskline)[0]
                self.__setattr__(attrib, value)

    def process_multi_value_attributes(self):
        multi_value_attribs = ['tags', 'contexts']
        for attrib in multi_value_attribs:
            attribRE = eval(r"TaskRE.{}".format(attrib))
            if re.search(attribRE, self.taskline):
                value = re.findall(attribRE, self.taskline)
                self.__setattr__(attrib, value)


    def parse_task(self):
        #other = [text for text in re.findall(TaskRE.task, self.taskline)]
        task = TaskRE.task.sub(r" ", str(self.taskline)).strip()
        #task = re.sub(r'\s+', ' ', task).strip()
        self.task = task

        return task

class CompletedTask(Task):

    def __init__(self, taskline, priority=None):
        super().__init__(self, taskline)
        self.priority = None
        self.completion_date = CompletedTask.get_completion_date(self)

    def get_completion_date(self):
        from datetime import date
        completion_date_RE = TaskRE.completion_date
        if re.search(completion_date_RE, self.taskline):
            self.completion_date = re.findall(completion_date_RE, self.taskline)[0]
        else:
            self.completion_date = date.today().isoformat()


class SomedayTask(Task):
    def __init__(self, taskline):
        super().__init__(self, taskline)
        self.priority = "C"
        self.completion_date = None
        self.threshold_date = None
        self.due_date = None
        self.someday = True

