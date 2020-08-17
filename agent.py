from enum import Enum 
from prob import *  


# S -> I -> R

stages = Enum("stage", "S I R")

class Agent:
    def __init__(self, id, init_stage): 
        self.id = id
        self.stage = None
        self.time_until_transition = None 
        self.p = 1/7500
        self.T_i = 15 

        self.set_stage(init_stage) 

    def set_stage(self, new_stage):
        self.stage = new_stage 
        if (self.stage == stages.I):
            exposed_time = expo(self.T_i) 
            # print("exposed_time = {}".format(exposed_time))
            self.set_time_until(exposed_time) 

    def set_time_until(self, trans_time):
        self.time_until_transition = trans_time 

    def get_time_until(self):
        return self.time_until_transition
    
    def reduce_time_until(self, timestep):
        if (self.time_until_transition != None):
            self.time_until_transition -= timestep 