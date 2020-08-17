from agents import * 

class Simulator:
    def __init__(self, NS, NI, NR):
        self.time = 0
        self.time_end = 5000
        self.timestep = 0.25 
        self.agents = Agents(NS, NI, NR) 
        self.prev_NS = NS
        self.prev_NI = NI
        self.prev_NR = NR 
        
    def run(self, print_every=True, print_end=True):
        while(self.time <= self.time_end and self.agents["I"] > 0):
            self.agents.step(self.timestep)
            if (print_every):
                if (self.prev_NS != self.agents["S"] or self.prev_NI != self.agents["I"] or self.prev_NR != self.agents["R"]):
                    print("t = {}:\t agents = {}".format(self.time, self.agents)) 
                self.prev_NS = self.agents["S"]
                self.prev_NI = self.agents["I"]
                self.prev_NR = self.agents["R"]

            self.time += self.timestep 

        if (print_end):
            print("==================")
            print("Duration: {} days \nEpidemic size: {}".format(self.time, self.agents["R"]))
    
    def get_results():
        return { "epidemic": self.agents["R"], "duration": self.time } 

if __name__ == "__main__":
    sim = Simulator(1000, 1, 0)
    sim.run() 

    

    