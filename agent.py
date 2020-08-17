from enum import Enum 
from prob import *  


# S -> I -> R

stages = Enum("stage", "S E I R")

class Agent:
    def __init__(self, id, init_stage, p=1/7500): 
        self.id = id
        self.time_until_transition = None 
        self.p = p 
        self.T_e = 5 
        self.T_i = 15 
        self.init_stage = init_stage 
        self.stage = None
        self.set_stage(init_stage) 

    def set_stage(self, new_stage):
        self.stage = new_stage 
        if (self.stage == stages.E):
            exposed_time = expo(self.T_e)
            self.set_time_until(exposed_time)
        elif (self.stage == stages.I):
            infectious_time = erlang(3, self.T_i) 
            self.set_time_until(infectious_time) 

    def get_stage(self):
        return self.stage 

    def reset(self):
        self.set_stage(self.init_stage)

    def set_time_until(self, trans_time):
        self.time_until_transition = trans_time 

    def get_time_until(self):
        return self.time_until_transition
    
    def reduce_time_until(self, timestep):
        if (self.time_until_transition != None):
            self.time_until_transition -= timestep 