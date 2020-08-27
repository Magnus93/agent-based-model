import sys
import pandas as pd
from aux_functions import * 


if __name__=="__main__":
    if len(sys.argv)>=3: 
        abm = pd.read_csv(sys.argv[1])
        css = pd.read_csv(sys.argv[2])

        keys = ["Range", "PDF", "CDF"]

        new_table = pd.DataFrame()
        for key in keys:
            if str(key) != "Unnamed":
                header = "ABM."+key
                print(header)
                new_table[header] = abm[key].tolist() 

        for key in keys:
            print(key) 
            if str(key) != "Unnamed":
                header = "CSS."+key
                print(header)
                new_table[header] = css[key].tolist() 

        print(new_table) 
        new_table.to_csv("p-p-plot-"+str(len(abm))+"bins.csv")

    else:
        print("Not enough arguments") 