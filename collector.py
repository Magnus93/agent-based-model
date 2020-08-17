# collects results from multible simulations 
from simulator import * 
import random 


N_sim = 50  



if __name__ == "__main__":
    for i in range(N_sim):
        print("--- iteration {} ---".format(i))
        sim = Simulator(1000, 1, 0) 
        sim.run(print_every=False, print_end=True)
