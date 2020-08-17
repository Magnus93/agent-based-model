from agent import *
import math 


class Agents(object):
    def __init__(self, num_s, num_i, num_r):
        self.init = { "S": num_s, "I": num_i, "R": num_r }
        self.agents = {}
        self.num_agents = 0 
        for stage in stages:
            self.agents[stage.name] = [] 

        for i in range(num_s):
            self.add_agent(stages.S)

        for i in range(num_i):
            self.add_agent(stages.I)

        for i in range(num_r):
            self.add_agent(stages.R)

    def reset(self):
        temp_agents = {} 
        for stage in stages:
            temp_agents[stage.name] = [] 

        for stage in stages:
            agts = self.agents[stage.name]
            for agent in agts:
                agent.reset()
                init_stage = agent.get_stage()
                temp_agents[init_stage.name].append(agent) 
        self.agents = temp_agents 

    def add_agent(self, stage):
        new_agent = Agent(self.num_agents, stage)
        self.agents[stage.name].append(new_agent)
        self.num_agents += 1 

    def move_individual(self, inv, dst_stage):
        src_stage = inv.stage
        self.agents[src_stage.name].remove(inv)
        self.agents[dst_stage.name].append(inv)
        inv.set_stage(dst_stage) 

    def step(self, timestep):
        p = 1/7500 
        NS = len(self.agents["S"])
        NI = len(self.agents["I"])
        NR = len(self.agents["R"])

        # loop through infectious and check if any become removed 
        for inv in self.agents["I"]:
            inv.reduce_time_until(timestep) 
            until = inv.get_time_until()
            if (type(until) is float and until < 0):
                self.move_individual(inv, stages.R) 

        # loop through suseptible and check their if any gets infected 
        for inv in self.agents["S"]:
            rand = random.random()
            risk = 1 - math.exp(timestep * NI * math.log(1-p))
            if rand < risk:
                self.move_individual(inv, stages.I)  

    def __getitem__(self, key):
        return len(self.agents[key]) 

    def __str__(self):
        string = ""
        for stage in stages:
            num = len(self.agents[stage.name])
            string += "{}: {}, \t".format(stage.name, num)
        return string 


if __name__ == "__main__":
    agents = Agents(1000, 1, 0, 0)
    print(agents)