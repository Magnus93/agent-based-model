import pandas as pd 
import numpy as np 

def sec_to_str(seconds):
    m = int(seconds//60)
    s = int(seconds%60)
    if m == 0:
        return "{} s".format(s)
    else:
        return "{} min {} s".format(m, s)


# filename without extension 
def save_pandas_dataframe_as_csv(df, filename):
    try:
        df.to_csv(filename+".csv")
    except:
        n = 1
        success = False 
        while not success:
            print("unsuccesful print "+str(n))
            try:
                stats.to_csv(filename + str(n) + ".csv")
                success = True 
                filename = filename + str(n) + ".csv"
            except:
                n += 1
    return print(str(filename)+".csv") 


def get_pdf(list_of_values):
    list_of_values.sort()
    return list_of_values 

def get_cdf(list_of_values):
    list_of_values.sort()
    values = np.array(list_of_values) 
    values = np.cumsum(values) / np.sum(values)

    return values.tolist() 