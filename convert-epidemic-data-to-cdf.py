# This script takes filename of csv file with css data and converts it to csv 

import sys
import pandas as pd
from aux_functions import * 


if __name__=="__main__":
    if len(sys.argv)>=2:
        data = pd.read_csv(sys.argv[1])
        data = data.sort_values(by="Epidemic")  
        new_data = pd.DataFrame(columns=["Range", "PDF", "CDF"])
        
        bins = 20
        minimum = 0
        maximum = 1000 

        hist = get_hist_pdf(data["Epidemic"].tolist(), bins, minimum, maximum)
        new_data["Range"] = hist[1][:bins]
        new_data["PDF"] = hist[0]
        new_data["CDF"] = get_hist_cdf(data["Epidemic"].tolist(), bins, minimum, maximum) 

        print(new_data) 

        filename = "css-density-"+str(len(data))+"reps-"+str(len(new_data))+"bins.csv"
        new_data.to_csv(filename)

        print("saved: \t"+filename) 
    else:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("-- input csv filename as argument to convert epidemic results to PDF and CDF --") 
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")