from agent import *
import math 


class Agents(object):
    def __init__(self, NS, NE, NI, NR):
        self.agents = [] 
        self.sizes = { "S": 0, "E": 0, "I": 0, "R": 0 }

        for i in range(NS):
            self.add_agent(stages.S)

        for i in range(NE):
            self.add_agent(stages.E)

        for i in range(NI):
            self.add_agent(stages.I)

        for i in range(NR): 
            self.add_agent(stages.R)

    def reset(self):
        self.sizes = { "S": 0, "E": 0, "I": 0, "R": 0 }
        for agent in self.agents:
            agent.reset()
            init_stage = agent.get_stage()
            self.sizes[init_stage.name] += 1

    def get_population_size(self):
        N = 0
        for stage in stages:
            N += self.sizes[stage.name]
        return N 

    def add_agent(self, stage):
        new_agent = Agent(self.get_population_size(), stage)
        self.agents.append(new_agent)
        self.sizes[stage.name] += 1

    def move_individual(self, inv, dst_stage):
        src_stage = inv.stage
        inv.set_stage(dst_stage) 
        self.sizes[src_stage.name] -= 1
        self.sizes[dst_stage.name] += 1

    def step(self, timestep):
        # get number of infectious before step 
        NI = self.sizes["I"] 

        for inv in self.agents:
            if (inv.get_stage() == stages.S):
                rand = random.random()
                risk = 1 - math.exp(timestep * NI * math.log(1-inv.p))
                if rand < risk:
                    self.move_individual(inv, stages.E) 
            elif (inv.get_stage() == stages.E):
                inv.reduce_time_until(timestep)
                until = inv.get_time_until()
                if (type(until) is float and until < 0):
                    self.move_individual(inv, stages.I) 
            elif (inv.get_stage() == stages.I):
                inv.reduce_time_until(timestep) 
                until = inv.get_time_until()
                if (type(until) is float and until < 0):
                    self.move_individual(inv, stages.R) 

    def __getitem__(self, key):
        return self.sizes[key]

    def __str__(self):
        string = ""
        for stage in stages:
            num = self[stage.name] 
            string += "{}: {}, \t".format(stage.name, num)
        return string 


if __name__ == "__main__":
    agents = Agents(1000, 1, 0, 0)
    print(agents)