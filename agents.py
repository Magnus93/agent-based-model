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
stages = ["S", "E", "I", "R"]


class Agents(object):
    def __init__(self, specs):
        self.agents = {} 
        self.num_agents = 0 
        for stage in stages:
            # create list for each stage 
            self.agents[stage] = []

        for spec in specs:
            for i in range(spec["amount"]):
                self.add_agent(spec)

    def add_agent(self, spec):
        new_agent = {
            "id":           self.num_agents,
            "init_stage":   spec["init_stage"],
            "stage":        spec["init_stage"],
            "time_until":   None,
            "group_name":   get_attr(spec, "group_name"),
            "p":            get_attr(spec, "p"),
            "Te":           get_attr(spec, "Te"),
            "Ti":           get_attr(spec, "Ti")
        }
        self.set_stage(new_agent, spec["init_stage"]) 
        self.agents[spec["init_stage"]].append(new_agent)
        self.num_agents += 1 

    def set_stage(self, agent, stage):
        agent["stage"] = stage 
        if (stage == "E"):
            agent["time_until"] = expo(agent["Te"])
        elif (stage == "I"): 
            agent["time_until"] = erlang(3, agent["Ti"]/3) 


    def move_individual(self, agent, dst_stage):
        src_stage = agent["stage"] 
        self.agents[src_stage].remove(agent)
        self.agents[dst_stage].append(agent)
        self.set_stage(agent, dst_stage) 

    def step(self, timestep):
        NI = len(self.agents["I"])

        # loop through infectious and check if any become removed 
        for agent in self.agents["I"]:
            agent["time_until"] -= timestep
            if (agent["time_until"] < 0):
                self.move_individual(agent, "R") 

        # loop through exposed agents 
        for agent in self.agents["E"]:
            agent["time_until"] -= timestep
            if (agent["time_until"] < 0):
                self.move_individual(agent, "I") 

        # loop through suseptible and check their if any gets infected 
        for agent in self.agents["S"]:
            uniform = random.random() 
            # dt*NI*ln(1-p) 
            risk = 1 - math.exp(timestep * NI * math.log(1-agent["p"]))
            if uniform < risk:
                self.move_individual(agent, "E")

    def get_num(self, stage, group_name=None):
        if group_name == None:
            return len(self.agents[stage])
        counter = 0
        for agent in self.agents[stage]:
            if agent["group_name"] == group_name:
                counter += 1 
        return counter  

    def __str__(self):
        string = ""
        for stage in stages:
            num = len(self.agents[stage])
            string += "{}: {}, \t".format(stage, num)
        return string 


if __name__ == "__main__":
    agents = Agents(1000, 1, 0, 0)
    print(agents)