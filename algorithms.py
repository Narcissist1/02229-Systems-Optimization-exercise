# Different algorithms required by the exercise

def dm_guarantee(tasks):
    '''
    Algorithm  for  testing  the  schedulabihty
    of  a  periodic  task  set  T  under  DeadHne  Monotonic.
    '''
    for task in tasks:
        I, R = 0, 0
        while(I + task.WCET > R):
            R = I + task.WCET
            if(R > tasks.deadline):
                return False
            # update I
    return True
