import sys 
import math 
import pandas as pd 
import statistics 
import numpy as np 


def get_list_of_stats(name, data_list):
    mean = statistics.mean(data_list) 
    stdev = statistics.stdev(data_list)
    # 1.96 for 95% confidence intervall
    sterror = 1.96*stdev / math.sqrt(len(data_list)-1) 
    return [
        name,
        mean,
        stdev,
        mean-sterror, 
        mean+sterror, 
        min(data_list),
        max(data_list),
    ]


if __name__=="__main__":
    print("Argument 1: model type")
    print("Argument 1: csv file")
    if len(sys.argv)>=3:
        file_path = sys.argv[1]+"/"+sys.argv[2]
        data = pd.read_csv(file_path)
        result = pd.DataFrame(columns=["name", "avg", "stdev", "95CI-", "95CI+", "min", "max"])
        for key in data:
            result.loc[len(result)] = get_list_of_stats(key, data[key].tolist())
            if (key == "Epidemic"):
                result.loc[len(result)] = get_list_of_stats("extinctions", (np.array(data[key]) < 100).tolist())
        print(result)
        result.to_csv(sys.argv[1]+'/'+sys.argv[1]+'-stats.csv')







