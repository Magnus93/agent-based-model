from enum import Enum 
from prob import *  

get_attr = lambda dct, key, default: dct[key] if key in dct else default  

# S -> I -> R

stages = Enum("stage", "S E I R")

default_p = 1/7500 

class Agent:
    def __init__(self, id, spec): 
        self.id = id
        self.time_until_transition = None 

        self.p = get_attr(spec, "p", default_p)
        self.group_name = get_attr(spec, "group_name", "noname")
        self.T_e = 5 
        self.T_i = 15 
        self.init_stage = stages[spec["init_stage"]]
        self.stage = None
        self.set_stage(self.init_stage) 

    def set_stage(self, new_stage):
        self.stage = new_stage 
        if (self.stage == stages.E):
            exposed_time = expo(self.T_e)
            self.set_time_until(exposed_time)
        elif (self.stage == stages.I):
            infectious_time = erlang(3, self.T_i/3) 
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