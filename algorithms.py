import math
import random
import numpy as np
from Entity import Solution


class Mapping:
    def __init__(self, tasks, cores, initTemperature, panelty=100000, r=0.001):
        self.tasks = tasks
        self.cores = cores
        self.panelty = panelty
        self.T = initTemperature
        self.r = r
        self.space = set()

    def dm_guarantee(self, core):
        '''
        Algorithm  for  testing  the  schedulabihty
        of  a  periodic  task  set  T  under  DeadHne  Monotonic.
        Based on Chapter 4, Figure 4.13
        https://dtudk-my.sharepoint.com/personal/paupo_win_dtu_dk/_layouts/15/onedrive.aspx?originalPath=aHR0cHM6Ly9kdHVkay1teS5zaGFyZXBvaW50LmNvbS86ZjovZy9wZXJzb25hbC9wYXVwb193aW5fZHR1X2RrL0VxaGZHQlM3NXR4RXNtcFgzMy1uYVFRQkswMnVYRzlSODBDMGJXOW1VWXlxYkE%5FcnRpbWU9SmxGYTFWNUsyRWc&id=%2Fpersonal%2Fpaupo%5Fwin%5Fdtu%5Fdk%2FDocuments%2Fteaching%2F02229%20E20%2Fweek%2038%2DTue%2E%20Sept%2E%2015%2D%2DReal%2Dtime%20systems%2FHard%20Real%2DTime%2D%2DPeriodic%20Scheduling%20chapter%2Epdf&parent=%2Fpersonal%2Fpaupo%5Fwin%5Fdtu%5Fdk%2FDocuments%2Fteaching%2F02229%20E20%2Fweek%2038%2DTue%2E%20Sept%2E%2015%2D%2DReal%2Dtime%20systems
        '''
        laxity = 0
        # update WCET for each task on this core
        for task in core.tasks:
            task.setWCETOnCore(task.WCET * core.WCETFactor)

        for task in core.tasks:
            I, R = 0, 0
            while(I + task.WCETOnCore > R):
                R = I + task.WCETOnCore
                if(R > task.deadline):
                    # unschedulable
                    core.setLaxity(self.panelty)
                    return None
                # update I
                _I = 0
                for t in core.tasks:
                    if t.priority > task.priority:
                        _I += math.ceil(R / t.period) * t.WCETOnCore
                I = _I
            laxity += task.deadline - R

        core.setLaxity(laxity)
        return laxity

    def generate_init_soluton(self):
        for task in self.tasks:
            core = random.choice(self.cores)
            core.addTask(task)

        return Solution(self.cores)

    def getNeighbor(self, solution):
        aCore = random.choice(solution.cores)
        while aCore.isEmpty():
            aCore = random.choice(solution.cores)
        bCore = random.choice(solution.cores)
        while aCore == bCore:
            bCore = random.choice(solution.cores)

        aTask = aCore.popTask()
        bCore.addTask(aTask)
        return solution

    def coolDown(self):
        self.T = self.T * (1 - self.r)

    def cost(self, solution):
        '''
        cost function to measure the quality of a solution
        '''
        laxity = 0
        for core in solution.cores:
            val = self.dm_guarantee(core)
            laxity += val if val is not None else - self.panelty

        solution.setLaxity(laxity)
        return laxity

    def accProbability(self, delta):
        try:
            ans = math.exp(abs(delta) / self.T)
        except OverflowError:
            ans = float('inf')
        return 1.0 / ans

    def run(self):
        '''
        Simulated Annealing algorithm goes here
        '''
        bestSolutionSofar = None
        curSolution = self.generate_init_soluton()
        self.cost(curSolution)
        self.space.add(hash(curSolution))
        while self.T > 1:
            neighbor = self.getNeighbor(curSolution)
            hashVal = hash(neighbor)
            if hashVal in self.space:
                continue
            else:
                self.space.add(hashVal)
            delta = self.cost(neighbor) - self.cost(curSolution)
            if delta > 0 or self.accProbability(delta) > np.random.uniform():
                curSolution = neighbor
                if bestSolutionSofar is None or bestSolutionSofar.laxity < curSolution.laxity:
                    bestSolutionSofar = curSolution
            self.coolDown()

        print("Explored {} solutions".format(len(self.space)))
        return bestSolutionSofar
