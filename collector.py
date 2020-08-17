# collects results from multible simulations 
from simulator import * 
import random 


N_sim = 1000 
seed = 1 



if __name__ == "__main__":
    sim = Simulator(1000, 1, 0)  
    
    for i in range(N_sim):
        sim.run(print_every=False, print_end=True)
