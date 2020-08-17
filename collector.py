# collects results from multible simulations 
from simulator import * 
import random 
import pandas as pd 
import time 

filename = "agent-based"
N_sim = 5000 
print_every = 20 

# Create the pandas DataFrame 
table = pd.DataFrame(columns = ['Duration', 'Epidemic']) 
data = pd.DataFrame() 

if __name__ == "__main__": 
    start_time = time.time()
    sim = Simulator(1000, 1, 0, 0) 
    for i in range(N_sim):
        sim.run(print_every=False, print_end=False)
        results = sim.get_results()
        table.loc[len(table)] = [results["duration"], results["epidemic"]] 
        sim.reset() 

        if i%print_every == 1:
            time_past = time.time() - start_time 
            eta =  time_past*(N_sim - i) / i   
            eta_m = int(eta//60)
            eta_s = int(eta%60) 
            print("iteration {}, \t eta: {} min {} s".format(i, eta_m, eta_s))

    
    exec_time = time.time() - start_time
    print("####### Collection DONE #######")
    print("Exec. time: \t{:.{prec}f} sec.".format(exec_time, prec=2))
    print("num. repl.: \t{}".format(N_sim))
    # sort table by epidemic size 
    table = table.sort_values(by="Epidemic")
    try:
        table.to_csv(filename+".csv")
    except:
        n = 1
        success = False 
        while not success:
            print("unsuccesful print "+str(n))
            try:
                table.to_csv(filename + str(n) + ".csv")
                success = True 
                filename = filename + str(n) + ".csv"
            except:
                n += 1
    print("result saved as: {}".format(filename))
