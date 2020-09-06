import math


class Mapping:
    def __init__(self, tasks, cores):
        self.tasks = tasks
        self.cores = cores

    def dm_guarantee(self, tasks):
        '''
        Algorithm  for  testing  the  schedulabihty
        of  a  periodic  task  set  T  under  DeadHne  Monotonic.
        Based on Chapter 4, Figure 4.13
        https://dtudk-my.sharepoint.com/personal/paupo_win_dtu_dk/_layouts/15/onedrive.aspx?originalPath=aHR0cHM6Ly9kdHVkay1teS5zaGFyZXBvaW50LmNvbS86ZjovZy9wZXJzb25hbC9wYXVwb193aW5fZHR1X2RrL0VxaGZHQlM3NXR4RXNtcFgzMy1uYVFRQkswMnVYRzlSODBDMGJXOW1VWXlxYkE%5FcnRpbWU9SmxGYTFWNUsyRWc&id=%2Fpersonal%2Fpaupo%5Fwin%5Fdtu%5Fdk%2FDocuments%2Fteaching%2F02229%20E20%2Fweek%2038%2DTue%2E%20Sept%2E%2015%2D%2DReal%2Dtime%20systems%2FHard%20Real%2DTime%2D%2DPeriodic%20Scheduling%20chapter%2Epdf&parent=%2Fpersonal%2Fpaupo%5Fwin%5Fdtu%5Fdk%2FDocuments%2Fteaching%2F02229%20E20%2Fweek%2038%2DTue%2E%20Sept%2E%2015%2D%2DReal%2Dtime%20systems
        '''
        for task in tasks:
            I, R = 0, 0
            while(I + task.WCET > R):
                R = I + task.WCET
                if(R > self.tasks.deadline):
                    return False
                # update I
                _I = 0
                for t in self.tasks:
                    if t.priority > task.priority:
                        _I += math.ceil(R / t.period) * t.WCET
                I = _I

        return True

    def generate_init_soluton(self):
        pass

    def getNeighbor(self):
        pass

    def coolDown(self):
        pass

    def cost(self):
        '''
        cost function to measure the quality of a solution
        '''
        pass

    def accProbability(self):
        pass

    def run(self):
        '''
        Simulated Annealing algorithm goes here
        '''
        pass
