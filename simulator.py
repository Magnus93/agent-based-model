from agents import * 
import pandas as pd  


class Simulator:
    def __init__(self, spec): 
        self.time = 0
        self.time_end = 5000
        self.timestep = 0.25 
        self.agents = Agents(spec) 
        self.prev_NS = self.agents.get_num("S")
        self.prev_NE = self.agents.get_num("E")
        self.prev_NI = self.agents.get_num("I")
        self.prev_NR = self.agents.get_num("R")
        self.save_data = False 
        self.table = pd.DataFrame(columns = ['time', 'S', 'E', 'I', 'R']) 
        
    def set_save_data(self, on):
        self.save_data = on 

    def store_to_table(self):
        if self.save_data:
            self.table.loc[len(self.table)] = [
                self.time,
                self.agents["S"],
                self.agents["E"],
                self.agents["I"],
                self.agents["R"]
            ]
    
    def run(self, print_every=True, print_end=True):
        self.store_to_table()

        while(self.time <= self.time_end and self.agents.get_num("E")+ self.agents.get_num("I") > 0):
            self.agents.step(self.timestep)

            if (self.prev_NS != self.agents.get_num("S") or \
                self.prev_NI != self.agents.get_num("I") or \
                self.prev_NI != self.agents.get_num("I") or \
                self.prev_NR != self.agents.get_num("R")):
                self.store_to_table() 
                if (print_every):
                    print(self)
            self.prev_NS = self.agents.get_num("S")
            self.prev_NE = self.agents.get_num("E")
            self.prev_NI = self.agents.get_num("I")
            self.prev_NR = self.agents.get_num("R")

            self.time += self.timestep 

        self.store_to_table()
        if (print_end):
            print("FINAL: \t"+str(self))
            print("==================")
            print("Duration: {} days \nEpidemic size: {}".format(self.time, self.agents.get_num("R")))
    
    def export_table(self):
        self.table.to_csv("simulation_result.csv")

    def __str__(self):
        return "t = {}:\t agents = {}".format(self.time, self.agents)

    def get_results(self):
        return { 
            "duration": self.time , 
            "epidemic": self.agents.get_num("R"),
            "R": {
                "high_risk": self.agents.get_num("R", "high_risk"),
                "low_risk": self.agents.get_num("R", "low_risk")
            }
        }

if __name__ == "__main__":
    
    specs = [
    {"amount": 500, "init_stage": "S", "p": 1/5000, "group_name": "high_risk"}, 
    {"amount": 500, "init_stage": "S", "p": 1/15000, "group_name": "low_risk"}, 
    {"amount": 1, "init_stage": "E"}
    ]
    sim = Simulator(specs)
    sim.run() 