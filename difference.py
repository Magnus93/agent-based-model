import sys 
import math 
import pandas as pd 
#import numpy as np 
import statistics 

num_data = 10000

attributes = ["Epidemic", "Duration", "Rt", "extinctions"]


def get_row_by_name(df, name):
    for index, row in df.iterrows():
        if (row["name"] == name):
            return row

if __name__=="__main__":
    print("argument 1: model type")
    print("argument 2: stats_file1.csv")
    print("argument 3: stats_file2.csv")
    if len(sys.argv)>=4:
        path = sys.argv[1]+"/" 
        stats1 = pd.read_csv(path+sys.argv[2])
        stats2 = pd.read_csv(path+sys.argv[3])
        diff_table = pd.DataFrame(columns=["name", "CI-", "CI+", "Zero_included"])
        for attribute in attributes:
            row1 = get_row_by_name(stats1, attribute)
            row2 = get_row_by_name(stats2, attribute)
            diff_avg = row1["avg"] - row2["avg"]
            diff_stdev = math.sqrt( \
            (row1["stdev"]**2)/(num_data-1) + \
            (row2["stdev"]**2)/(num_data-1) \
            )
            lamda = 1.96  # 95% confidence 
            diff_min = diff_avg - lamda * diff_stdev
            diff_max = diff_avg + lamda * diff_stdev
            zero_included = diff_min < 0 < diff_max 
            diff_table.loc[len(diff_table)] = [attribute, diff_min, diff_max, zero_included]
        print(diff_table)
        file_dest = path+"diff_table.csv"
        diff_table.to_csv(file_dest)
        print("saved: "+file_dest)

