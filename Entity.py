# Class representation of the input data

class Task:
    def __init__(self, _id, deadline, period, WCET):
        self.id = _id
        self.deadline = float(deadline)
        self.period = float(period)
        self.WCET = float(WCET)
        self.WCRT = 0  # update during the calculation
        self.priority = 1.0 / self.deadline
        self.WCETOnCore = 0  # update during the calculation

    def setPriority(self, val):
        self.priority = val

    def setWCRT(self, val):
        self.WCRT = val

    def setWCETOnCore(self, val):
        self.WCETOnCore = val


class Core:
    def __init__(self, _id, pid, WCETFactor):
        self.id = _id
        self.platformId = pid
        self.WCETFactor = float(WCETFactor)
        self.tasks = set()  # tasks that were assigned to the current core

    def addTask(self, task):
        self.tasks.add(task)

    def removeTask(self, task):
        self.tasks.remove(task)


class Solution:
    def __init__(self, cores):
        self.cores = cores
        self.laxity = 0

    def setLaxity(self, val):
        self.laxity = val
