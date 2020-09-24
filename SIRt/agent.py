import math 
from prob import *

defaults = { 
    "p": 1/7500, 
    "Te": 5,
    "Ti": 15, 
    "group_name": "noname" 
}
get_attr = lambda dct, key: dct[key] if key in dct else defaults[key]   

# S -> E -> I -> R
stages = ["S", "I", "R"]


class Agent:
    def __init__(self, id, spec, time):  
        self.stage = spec["init_stage"]
        self.p = get_attr(spec, "p") 
        self.time_to_leave = None
        self.group_name = get_attr(spec, "group_name")
        self.p = get_attr(spec, "p")
        self.Te = get_attr(spec, "Te")
        self.Ti = get_attr(spec, "Ti")

        self.set_stage(spec["init_stage"], time) 

    def set_stage(self, new_stage, time):
        self.stage = new_stage 
        if (new_stage == "I"):
            self.time_to_leave = time + expo(self.Ti)

    def get_stage(self):
        return self.stage 

    def get_group_name(self):
        return self.group_name 

    def step(self, time, timestep, NI):
        if (self.stage == "S"):
            uniform = random.random()
            risk = 1 - math.exp(timestep * NI * math.log(1-self.p))
            if uniform <= risk:
                self.set_stage("I", time)
        
        elif (self.stage == "I"):
            # -timestep/2 removes bias so trigger time is time_to_leave +/- timestep/2. 
            if (self.time_to_leave - timestep/2 <= time):
                self.set_stage("R", time) 


                