import sys 
import pandas as pd 
import statistics 
import numpy as np 
import matplotlib.pyplot as plt 

print("import done")

model_type = "2SEI3RtipAed"
csv_abm = "abm-data-seed12310-10000.csv"
csv_css = "css-data-seed12310-10000.csv"

dimension = "Rt"

def prob_list(np_arr, max_value):
    result = [] 
    divs = 30 
    size = len(np_arr)
    for i in range(divs):
        temp = np.sum(np_arr < i*(max_value/divs))/size 
        result.append(temp)
    return result 
    


if __name__=="__main__":
    print("running pp-plot")
    ep_abm = pd.read_csv("./"+model_type+"/"+csv_abm)[dimension].to_numpy()
    ep_css = pd.read_csv("./"+model_type+"/"+csv_css)[dimension].to_numpy()
    print(dimension+" values for ABM and CSS")
    print(ep_abm)
    print(ep_css)

    max_abm = np.max(ep_abm)
    max_css = np.max(ep_css)
    max_val = max(max_abm, max_css)
    print("maximum value is "+str(max_val))

    prob_abm = prob_list(ep_abm, max_val)
    prob_css = prob_list(ep_css, max_val)
    print("probablility for ABM and CSS")
    print(prob_abm)
    print(prob_css)


    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

    plt.plot([0, 1],[0, 1])
    plt.plot(prob_css, prob_abm, "rx")
    plt.ylabel("ABM")
    plt.xlabel("CSS")
    plt.title(dimension+" p-p-plot")
    plt.legend(["Reference line","Values"])
    plt.show()
