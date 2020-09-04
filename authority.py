import random 

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

    def step(self, time, timestep, I):
        # esitmate number of infectious 
        if (I > self.limit * self.pop_size):
            self.preventive_measures = True

    def get_p_factor(self):
        if (self.preventive_measures):
            return 0.5
        else:
            return 1
    