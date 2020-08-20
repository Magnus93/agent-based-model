import math 
from prob import *
from authority import * 
from agent import * 

class Agents(object):
    def __init__(self, specs, time): 
        self.agents = []  

        for spec in specs:
            for i in range(spec["amount"]):
                self.add_agent(spec, time)

        self.authority = Authority(len(self.agents)) 

    def add_agent(self, spec, time): 
        new_agent = Agent(len(self.agents), spec, time)  
        new_agent.set_stage(spec["init_stage"], time) 
        self.agents.append(new_agent)

    def new_p_factor(self): 
        self.p_factor = random.uniform(0.5, 1.5)  

    def step(self, time, timestep):
        NI = self.get_num("I") 

        self.authority.step(time, timestep, NI)

        if (time%7 < timestep):
            self.new_p_factor()  


        for agent in self.agents:
            agent.step(time, timestep, NI, self.p_factor, self.authority) 

    def get_num(self, stage, group_name=None):
        counter = 0
        if group_name == None:
            for agent in self.agents:
                if (agent.get_stage() == stage):
                    counter += 1 
            return counter 
        else:
            for agent in self.agents:
                if self.agents.get_stage() == stage:
                    if agent.get_group_name() == group_name:
                        counter += 1 
            return counter  

    def __str__(self):
        counters = { "S": 0, "E": 0, "I": 0, "R": 0 }
        for agent in self.agents:
            counters[agent.get_stage()] += 1
            
        return str(counters)


if __name__ == "__main__":
    agents = Agents(1000, 1, 0, 0)
    print(agents)