# Class representation of the input data
import random
from collections import deque


class Task:
    def __init__(self, _id, deadline, period, WCET):
        self.id = _id
        self.deadline = float(deadline)
        self.period = float(period)
        self.WCET = float(WCET)
        self.priority = 1.0 / self.deadline
        self.WCETOnCore = 0  # update during the calculation

    def setPriority(self, val):
        self.priority = val

    def setWCETOnCore(self, val):
        self.WCETOnCore = val


class Core:
    def __init__(self, _id, pid, WCETFactor):
        self.id = _id
        self.platformId = pid
        self.WCETFactor = float(WCETFactor)
        self.laxity = 10000  # initial laxity
        self.tasks = deque()  # tasks that were assigned to the current core

    def setLaxity(self, val):
        self.laxity = val

    def addTask(self, task):
        self.tasks.append(task)

    def popTask(self):
        if not self.tasks:
            raise ValueError
        task = random.choice(self.tasks)
        self.tasks.remove(task)
        return task

    def isEmpty(self):
        return True if len(self.tasks) == 0 else False


class Solution:
    def __init__(self, cores):
        self.cores = cores
        self.laxity = 0

    def setLaxity(self, val):
        self.laxity = val

    def __hash__(self):
        coreHashStrs = []
        for core in self.cores:
            if len(core.tasks) == 0:
                continue
            coreHashStrs.append(core.platformId + ':' + core.id + ':' +
                                ','.join(sorted([task.id for task in core.tasks])))
        return hash("#".join(coreHashStrs))
