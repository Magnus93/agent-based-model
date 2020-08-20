# collects results from multible simulations 
from simulator import * 
import random 
import pandas as pd 
import time 
from aux_funtions import * 
from prob import * 
import matplotlib.pyplot as plt 


filename = "agent-based"
N_sim = 100 
print_every = 10

NS = 1000 

# Create the pandas DataFrame 
table = pd.DataFrame(columns = ['Duration', 'Epidemic', 'Removed high risk', 'Removed low risk']) 
data = pd.DataFrame() 


if __name__ == "__main__": 
    start_time = time.time()
    
    for i in range(N_sim):
        N_high = binomial(NS, 0.5) 
        specs = [
            {"amount": N_high, "init_stage": "S", "p": 1/5000,  "group_name": "high_risk" }, 
            {"amount": NS-N_high, "init_stage": "S", "p": 1/15000, "group_name": "low_risk" }, 
            {"amount": 1, "init_stage": "E"}
        ]
        sim = Simulator(specs) 

        sim.run(print_every=False)

        table.loc[len(table)] = [
            sim.time,
            sim.get_num("R"),
            sim.get_num("R", "high_risk"),
            sim.get_num("R", "low_risk")
        ] 

        if i%print_every == 0 and i != 0:
            time_past = time.time() - start_time 
            eta =  time_past*(N_sim - i) / i   
            print("iteration {}, \t eta: {}".format(i, sec_to_str(eta)))

    
    exec_time = time.time() - start_time
    print("####### Collection DONE #######")
    print("Exec. time: \t{}".format(sec_to_str(exec_time)))
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

    plt.hist(table["Epidemic"].tolist(), bins=3)
    plt.show() 


