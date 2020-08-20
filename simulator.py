import math 
import pandas as pd
import matplotlib.pyplot as plt 
from prob import *
from authority import * 
from agent import * 



class Simulator:
    def __init__(self, specs): 
        self.time = 0
        self.timestep = 0.25 
        self.agents = []
        self.save = False 
        self.table = pd.DataFrame(columns = ['time', 'S', 'E', 'I', 'R'])

        for spec in specs:
            for i in range(spec["amount"]):
                self.add_agent(spec)

        self.authority = Authority(len(self.agents)) 

    def add_agent(self, spec): 
        new_agent = Agent(len(self.agents), spec, self.time)  
        new_agent.set_stage(spec["init_stage"], self.time) 
        self.agents.append(new_agent)

    def new_p_factor(self): 
        self.p_factor = random.uniform(0.5, 1.5)  

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

        self.authority.step(self.time, self.timestep, NI)

        if (self.time%7 < self.timestep):
            self.new_p_factor()  

        for agent in self.agents:
            agent.step(self.time, self.timestep, NI, self.p_factor, self.authority) 


    def get_all_num(self):
        counters = { "S": 0, "E": 0, "I": 0, "R": 0 }
        for agent in self.agents:
            counters[agent.get_stage()] += 1
        return counters 

    def get_num(self, stage, group_name=None):
        counter = 0
        if group_name == None:
            for agent in self.agents:
                if (agent.get_stage() == stage):
                    counter += 1 
            return counter 
        else:
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
        plt.legend(["S", "E", "I", "R"])
        plt.xlabel("time")
        plt.ylabel("agents") 
        plt.show() 

if __name__ == "__main__":
    specs = [
        {"amount": 500, "init_stage": "S", "p": 1/5000, "group_name": "high_risk"}, 
        {"amount": 500, "init_stage": "S", "p": 1/15000, "group_name": "low_risk"}, 
        {"amount": 1, "init_stage": "E"}
    ]
    sim = Simulator(specs)  
    sim.store_simulation(True) 
    sim.run(print_every=False)
    print(sim)
    print("number of REMOVED high risk {}".format(sim.get_num("R", "high_risk")))
    print("number of REMOVED low risk {}".format(sim.get_num("R", "low_risk")))
    sim.plot()