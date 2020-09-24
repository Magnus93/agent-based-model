import math 
import random
import pandas as pd
import matplotlib.pyplot as plt 
from prob import *
from agent import * 

class Simulator:
    def __init__(self, pop_specs): 
        self.time = 0
        self.timestep = 0.25 
        # keep track of how many individuals in each stage to save on computation time 
        self.sizes = { "S": 0, "E": 0, "I": 0, "R": 0 } 
        # list of all agents 
        self.agents = []
        # save data for each time step 
        self.save = False 
        self.p_uncert = random.uniform(0.75, 1.25)
        self.table = pd.DataFrame(columns = ['time', 'S', 'E', 'I', 'R'])

        for spec in pop_specs:
            for i in range(spec["amount"]):
                self.add_agent(spec)

    def add_agent(self, spec): 
        new_agent = Agent(len(self.agents), spec, self.time)  
        self.agents.append(new_agent)
        self.sizes[spec["init_stage"]] += 1 

    def store_simulation(self, save_bool=True):
        self.save = save_bool

    def store_time(self):
        nums = self.get_all_num()
        self.table.loc[len(self.table)] = [
            self.time,
            nums["S"],
            nums["E"],
            nums["I"],
            nums["R"]
        ]

    def run(self, print_every=True):
        while (self.get_num("E")+self.get_num("I") > 0):
            self.step() 
            if (print_every):
                print(self) 
            if (self.save):
                self.store_time()
            self.time += self.timestep 


    def step(self):
        NI = self.get_num("I") 

        for agent in self.agents:
            pre_stage = agent.get_stage() 
            agent.step(self.time, self.timestep, NI, self.p_uncert) 
            post_stage = agent.get_stage() 
            if (pre_stage != post_stage):
                self.sizes[pre_stage]  -= 1
                self.sizes[post_stage] += 1

    def get_population(self):
        population = 0
        for key in self.sizes:
            population += self.sizes[key]
        return population

    def get_all_num(self):
        return self.sizes 

    def get_num(self, stage, group_name=None):
        if group_name == None:
            return self.sizes[stage] 
        else:
            counter = 0
            for agent in self.agents:
                if agent.get_stage() == stage:
                    if agent.get_group_name() == group_name:
                        counter += 1 
            return counter  

    def __str__(self):
        return "time = "+str(self.time)+":\t"+str(self.get_all_num())

    def plot(self):
        plt.plot( \
            self.table["time"].tolist(), self.table["S"].tolist(), "g-",\
            self.table["time"].tolist(), self.table["E"].tolist(), "m-",\
            self.table["time"].tolist(), self.table["I"].tolist(), "r-",\
            self.table["time"].tolist(), self.table["R"].tolist(), "b-",\
        )
        plt.legend(["S", "I", "R"])
        plt.xlabel("time")
        plt.ylabel("agents") 
        plt.show() 

if __name__ == "__main__":
    specs = [
        {"amount": 1000, "init_stage": "S"}, 
        {"amount": 1, "init_stage": "E"}
    ]
    sim = Simulator(specs)  
    sim.store_simulation(True) 
    sim.run(print_every=False)
    print(sim)
    sim.plot()