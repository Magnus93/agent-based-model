from prob import *
import sys 
import pandas as pd 


if __name__=="__main__":
    print("Argument 1: csv file")
    if len(sys.argv)>=2:
        data = pd.read_csv(sys.argv[1])
        result = pd.DataFrame(columns=["name", "avg", "stdev", "95conf.Int.", "min", "max"])
        for key in data:
            result.loc[len(result)] = get_list_of_stats(key, data[key].tolist())
        print(result)







