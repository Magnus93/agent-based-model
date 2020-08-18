from agent import *
import math 


class Agents(object):
    def __init__(self, specs):
        self.agents = {} 
        self.num_agents = 0 
        for stage in stages:
            self.agents[stage.name] = [] 

        for spec in specs:
            for i in range(spec["amount"]):
                self.add_agent(spec)  

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

    def add_agent(self, spec):
        p = None 
        if "p" in spec:
            p = spec["p"]
        new_agent = Agent(self.num_agents, spec)
        self.agents[spec["init_stage"]].append(new_agent)
        self.num_agents += 1 

    def move_individual(self, inv, dst_stage):
        src_stage = inv.stage
        self.agents[src_stage.name].remove(inv)
        self.agents[dst_stage.name].append(inv)
        inv.set_stage(dst_stage) 

    def step(self, timestep):
        NI = len(self.agents["I"])

        # loop through infectious and check if any become removed 
        for inv in self.agents["I"]:
            inv.reduce_time_until(timestep) 
            until = inv.get_time_until()
            if (type(until) is float and until < 0):
                self.move_individual(inv, stages.R) 

        # loop through exposed agents 
        for inv in self.agents["E"]:
            inv.reduce_time_until(timestep)
            until = inv.get_time_until()
            if (type(until) is float and until < 0):
                self.move_individual(inv, stages.I) 


        # loop through suseptible and check their if any gets infected 
        for inv in self.agents["S"]:
            rand = random.random()
            risk = 1 - math.exp(timestep * NI * math.log(1-inv.p))
            if rand < risk:
                self.move_individual(inv, stages.E)  

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