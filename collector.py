# collects results from multible simulations 
from simulator import * 
import random 
import math 
import pandas as pd 
import sys
import statistics
import time 
from aux_funtions import * 
from prob import * 
import matplotlib.pyplot as plt  


N_sim = 30
if len(sys.argv) >= 2:
    N_sim = int(sys.argv[1]) 
print_every = 10

NS = 1000 
epidemic_limit = 0.1*NS 

skip_if_no_epidemic = False   

# Create the pandas DataFrame 
table = pd.DataFrame(columns = ['Duration', 'Epidemic', 'Removed high risk', 'Removed low risk']) 

if __name__ == "__main__": 
    start_time = time.time()
    
    # count the number of replications 
    i = 0  
    skipped = 0 
    below_epidemic_limit = 0 

    while i < N_sim:
        N_high = binomial(NS, 0.5) 
        N_low = NS - N_high
        specs = [
            {"amount": N_high, "init_stage": "S", "p": 1/5000,  "group_name": "high_risk" }, 
            {"amount": N_low, "init_stage": "S", "p": 1/15000, "group_name": "low_risk" }, 
            {"amount": 1, "init_stage": "E"}
        ]
        sim = Simulator(specs) 

        sim.run(print_every=False)

        epidemic_size = NS - sim.get_num("S") 

        if (skip_if_no_epidemic and epidemic_size < epidemic_limit):
            skipped += 1  
        else:
            i += 1 
            table.loc[len(table)] = [
                sim.time,
                epidemic_size,  
                N_high - sim.get_num("S", "high_risk"),
                N_low - sim.get_num("S", "low_risk") 
            ] 
            if (epidemic_size < epidemic_limit):
                below_epidemic_limit += 1  

        if i%print_every == 0 and i != 0:
            time_past = time.time() - start_time 
            eta =  time_past*(N_sim - i) / i   
            print("iteration {}, \t eta: {}, \t skipped: {}".format(i, sec_to_str(eta), skipped))

    stats = pd.DataFrame(columns = [
        'Measurement', 'mean', 'Std. Dev', 'Conf. Int (avg)', 'Min', 'Max', 
    ])

    mean = statistics.mean(table['Duration'].tolist()) 
    stdev = statistics.stdev(table['Duration'].tolist())
    sterror = stdev / math.sqrt(N_sim-1) 
    stats.loc[len(stats)] = [
        'Duration',
        mean,
        stdev,
        str(mean-sterror)+"  -  "+str(mean+sterror),
        min(table['Duration'].tolist()),
        max(table['Duration'].tolist()),
    ]

    mean = statistics.mean(table['Epidemic'].tolist()) 
    stdev = statistics.stdev(table['Epidemic'].tolist())
    sterror = stdev / math.sqrt(N_sim-1) 
    stats.loc[len(stats)] = [
        'Epidemic',
        mean,
        stdev,
        str(mean-sterror)+"  -  "+str(mean+sterror),
        min(table['Epidemic'].tolist()),
        max(table['Epidemic'].tolist()),
    ]

    exec_time = time.time() - start_time
    print("####### Collection DONE #######")
    print("Exec. time: \t{}".format(sec_to_str(exec_time)))
    print("num. repl.: \t{}".format(N_sim))
    print("Skipped replications: \t{}".format(skipped)) 
    print("Replications without epidemics: \t{}".format(below_epidemic_limit)) 
    filename = save_pandas_dataframe_as_csv(table.sort_values(by="Epidemic"), "agent-based-table")
    print("Table saved as: {}".format(filename))
    filename = save_pandas_dataframe_as_csv(stats, "agent-based-stats")
    print("Stats saved as: {}".format(filename))
    filename = save_pandas_dataframe_as_csv(pd.DataFrame(data={ 'cdf': get_cdf(table["Epidemic"].tolist()) }), "agent-based-cdf")

    # plt.hist(table["Epidemic"].tolist(), bins=10)
    plt.plot(get_pdf(table["Epidemic"].tolist()), get_cdf(table["Epidemic"].tolist()))
    plt.show() 


