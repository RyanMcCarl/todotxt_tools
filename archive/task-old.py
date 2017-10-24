import enum
import re

class TaskConfig(object):
    default_priority = 'B'
    lowest_priority = 'C'


class Regexes(enum.Enum):
    completed = re.compile(r'^(?P<COMPLETED>\s?x\s)')

    priority = re.compile(r'\(([A-Z])\)')
    someday = re.compile(r'@\b(?P<SOMEDAY>someday)\b')
    tags = re.compile(r'(?<=\+)(?P<TAG>(\w+))')
    taskline = re.compile(r'^(.*)$')

    # If the context starts with a number, it is treated as effort
    context = re.compile(r'@\b(?P<CONTEXT>\D+)\b')
    effort = re.compile(r'(?!<=@)(?P<NUMBER>\d+)(?P<UNITS>(?P<MINUTES>min)|(?P<HOURS>hours)|(?P<WEEKS>w))\b')

    # Dates
    creationdate = re.compile(r'(?!=^(?:x? )?\([A-Z]\) )(?P<CREATIONDATE>\b\d{4}-\d{2}-\d{2}\b)')
    thresholddate = re.compile(r'(?!<=t:)(?P<DUEDATE>\d{4}-\d{2}-\d{2})')
    duedate = re.compile(r'(?!<=due:)(?P<DUEDATE>\d{4}-\d{2}-\d{2})')
    completiondate = re.compile('(?![x\s\)\(A-Z]+(?P<CREATIONDATE>\b\d{4}-\d{2}-\d{2}\b) )(?P<COMPLETIONDATE>\b\d{4}-\d{2}-\d{2}\b)')
    isodate = re.compile(r'(\b\d{4}-\d{2}-\d{2}\b)')
    baddate = re.compile(r'\b(\d{1,2}/\d{1,2}/\d{1,2})\b')

    # Utility
    spaces = re.compile(r'\s+')


class Task(object):

    def __init__(self, taskline, priority='B', completed='False', creationdate=None, thresholddate=None,
        duedate=None, effort=None, tags=[], contexts=[]):
        self.taskline = taskline
        self.priority = priority
        self.completed = completed

        Task.is_completed(self)
        Task.parse_priority(self)

    def __str__(self):
        return "{0}".format(self.taskline)

    def __repr__(self):
        return """Task: {0}
        Properties: {1}\n\n""".format(self.taskline, vars(self))

    def is_completed(self):
        completedRE = Regexes.completed.value
        if completedRE.search(self.taskline):
            self.completed = True
            #return True


    def _parse_priority(self):
        priorityRE = Regexes.priority.value
        if priorityRE.search(self.taskline):
            _priority = priorityRE.search(self.taskline).group()
            self.priority = _priority
            #return _priority

    @property
    def completed(self):
        return self._completed


    @completed.setter
    def completed(self, completed='False'):
        self._completed = completed


    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority='B'):
        self._priority = priority


    @property
    def tags(self):
        return self.tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags


    @property
    def effort(self):
        return self.effort

    @effort.setter
    def effort(self, effort):
        self._effort = effort


    @property
    def context(self):
        return self.context

    @context.setter
    def context(self, context):
        self._context = context


    @property
    def creationdate(self):
        return self.creationdate

    @creationdate.setter
    def creationdate(self, creationdate):
        self._creationdate = creationdate


    @property
    def thresholddate(self):
        return self.thresholddate

    @thresholddate.setter
    def thresholddate(self, thresholddate):
        self._thresholddate = thresholddate


    @property
    def duedate(self):
        return self.duedate

    @duedate.setter
    def duedate(self, duedate):
        self._duedate = duedate

class CompletedTask(Task):

    def __init__(self, taskline, priority=None):
        super().__init__(self, taskline)
        self.priority = None

    @property
    def completiondate(self):
        return self.completiondate

    @completiondate.setter
    def completiondate(self, completiondate):
        self._completiondate = completiondate


class SomedayTask(Task):
    def __init__(self, taskline, priority='C'):
        super().__init__(self, taskline)
        self._priority = TaskConfig.lowest_priority
        self._completiondate = None
        self._thresholddate = None
        self._someday = True

