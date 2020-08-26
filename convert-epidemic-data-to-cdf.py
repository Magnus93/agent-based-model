# This script takes filename of csv file with css data and converts it to csv 

import sys
import pandas as pd
from aux_functions import * 


if __name__=="__main__":
    if len(sys.argv)>=2:
        data = pd.read_csv(sys.argv[1])
        data = data.sort_values(by="Epidemic")  
        new_data = pd.DataFrame(columns=["PDF", "CDF"])

        new_data["PDF"] = get_pdf(data["Epidemic"].tolist())
        new_data["CDF"] = get_cdf(data["Epidemic"].tolist())

        print(new_data) 

        filename = "css-density-"+str(len(new_data))+".csv"
        new_data.to_csv(filename)

        print("saved: \t"+filename) 
    else:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("-- input csv filename as argument to convert epidemic results to PDF and CDF --") 
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")