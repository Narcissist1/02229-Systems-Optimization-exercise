# Class representation of the input data

class Task:
    def __init__(self, _id, deadline, period, WCET):
        self.id = _id
        self.deadline = deadline
        self.period = period
        self.WCET = WCET
        self.priority = 1.0 / deadline


class Core:
    def __init__(self, _id, WCETFactor):
        self.id = _id
        self.WCETFactor = WCETFactor


class Platform:
    def __init__(self, _id):
        self.id = _id
        self.cores = []

    def addCore(self, core):
        if core:
            self.cores.append(core)
