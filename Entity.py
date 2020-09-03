# Class representation of the input data

class Task:
    def __init__(self, _id, deadline, period, WCET):
        self.id = _id
        self.deadline = float(deadline)
        self.period = float(period)
        self.WCET = float(WCET)
        self.priority = 1.0 / self.deadline


class Core:
    def __init__(self, _id, pid, WCETFactor):
        self.id = _id
        self.platformId = pid
        self.WCETFactor = float(WCETFactor)
        self.tasks = set()  # tasks that were assigned to the current core

    def addTask(self, task):
        self.tasks.add(task)


class SolutionTask:
    def __init__(self, _id, MCP, core, WCRT):
        self.id = _id
        self.MCP = MCP
        self.core = core
        self.WCRT = WCRT
