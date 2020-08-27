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
    return str(filename)+".csv" 


def get_pdf(list_of_values):
    list_of_values.sort()
    return list_of_values 

def get_cdf(list_of_values):
    list_of_values.sort()
    values = np.array(range(1,len(list_of_values)+1))/len(list_of_values) 
    return values.tolist() 

def get_hist_pdf(list_of_values, bins, mini, maxi):
    hist = np.histogram(list_of_values, bins=bins, range=(mini, maxi))
    pdf = (hist[0]/np.sum(hist[0]), hist[1])
    return pdf  

def get_hist_cdf(list_of_values, bins, mini, maxi): 
    hist = np.histogram(list_of_values, bins=bins, range=(mini, maxi))
    hist_values = hist[0]
    return np.cumsum(hist_values)/np.sum(hist_values) 