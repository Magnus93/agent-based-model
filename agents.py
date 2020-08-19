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
    def __init__(self, specs, time): 
        self.agents = {} 
        self.num_agents = 0 
        for stage in stages:
            # create list for each stage 
            self.agents[stage] = []

        for spec in specs:
            for i in range(spec["amount"]):
                self.add_agent(spec, time)

    def add_agent(self, spec, time): 
        new_agent = {
            "id":           self.num_agents,
            "init_stage":   spec["init_stage"],
            "stage":        spec["init_stage"],
            "time_to_leave":None, 
            "group_name":   get_attr(spec, "group_name"),
            "p":            get_attr(spec, "p"),
            "Te":           get_attr(spec, "Te"),
            "Ti":           get_attr(spec, "Ti")
        }
        self.set_stage(new_agent, spec["init_stage"], time) 
        self.agents[spec["init_stage"]].append(new_agent)
        self.num_agents += 1 

    def set_stage(self, agent, stage, time): 
        agent["stage"] = stage 
        if (stage == "E"):
            agent["time_to_leave"] = time + expo(agent["Te"])
        elif (stage == "I"): 
            agent["time_to_leave"] = time + erlang(3, agent["Ti"]/3) 

    def new_p_factor(self): 
        self.p_factor = random.uniform(0.5, 1.5) 

    def move_agent(self, agent, dst_stage, time):
        src_stage = agent["stage"] 
        self.agents[src_stage].remove(agent)
        self.agents[dst_stage].append(agent)
        self.set_stage(agent, dst_stage, time)  

    def step(self, time, timestep):
        NI = len(self.agents["I"])

        # loop through infectious and check if any become removed 
        for agent in self.agents["I"]:
            if (agent["time_to_leave"] < time):
                self.move_agent(agent, "R", time)  

        # loop through exposed agents 
        for agent in self.agents["E"]:
            if (agent["time_to_leave"] < time): 
                self.move_agent(agent, "I", time)  

        # loop through suseptible and check their if any gets infected 
        for agent in self.agents["S"]:
            uniform = random.random() 
            p = agent["p"]*self.p_factor 
            # dt*NI*ln(1-p) 
            risk = 1 - math.exp(timestep * NI * math.log(1-p))
            if uniform < risk:
                self.move_agent(agent, "E", time) 

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