import random 

class Authority:
    def __init__(self, population_size):
        self.p_factor = 1 
        # estimated infectious 
        self.est_infectious = 0 
        # poulation size 
        self.pop_size = population_size 
        # delay 
        self.delay = 7  


    def step(self, time, timestep, I):
        if (time%7 < timestep):
            self.delay = random.triangular(3, 7, 5)

        if ( 7-self.delay <= time%7 < 7-self.delay+timestep ):
            print("authority esitmation day: {}".format(time%7))
            self.est_infectious = I 
            if (self.est_infectious > 0.1*self.pop_size):
                self.p_factor = 0.5 
            else:
                self.p_factor = 1 


    def get_p_factor(self):
        return self.p_factor 
    