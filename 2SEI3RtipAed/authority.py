import random 
from prob import * 

class Authority:
    def __init__(self, population_size):
        # estimated infectious 
        self.est_infectious = 0 
        # poulation size 
        self.pop_size = population_size 
        
        # percent limit of infectious in the population 
        # if the limit is past then preventive measures start 
        self.limit = 0.05
        self.preventive_measures = False 
        self.time_of_prevention = 0 
        self.above_limit = False 
        self.delay = 0

    def step(self, time, timestep, I): 
        if (time%1 < timestep):
            # estimate number of infectious once per day 
            self.est_infectious = I * random.normalvariate(1, 0.25)

        if (self.above_limit == False):
            if (self.est_infectious > self.limit * self.pop_size):
                self.time_of_prevention = time + self.delay 
                self.above_limit = True
        
        if (self.above_limit):
            if (time-timestep/2 <= self.time_of_prevention < time+timestep/2):
                self.preventive_measures = True

    def get_p_factor(self):
        if (self.preventive_measures):
            return 0.5
        else:
            return 1
    