import random 

class Authority:
    def __init__(self, population_size, on=True):
        # estimated infectious 
        self.est_infectious = 0 
        # poulation size 
        self.pop_size = population_size 
        # is authority on or not 
        self.on = on 
        
        # percent limit of infectious in the population 
        # if the limit is past then preventive measures start 
        self.limit = 0.04
        self.preventive_measures = False 

    def step(self, time, timestep, I):
        if (self.on):
            # esitmate number of infectious 
            if (time%7 < timestep):
                sigma = 0.25
                bias = max(0, random.normalvariate(1, sigma))
                self.est_infectious = I*bias 

            if (not self.preventive_measures):
                delay = random.triangular(3, 7, 5)
                # 3-7 days to process estimation and take preventive measures 
                if ( delay <= time%7 < delay + timestep):
                    if (self.est_infectious > self.limit * self.pop_size):
                        self.preventive_measures = True 

    def get_p_factor(self):
        if (self.on):
            if (self.preventive_measures):
                return 0.5
            else:
                return 1
        else: 
            return 1 
    