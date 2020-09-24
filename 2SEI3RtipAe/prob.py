import random
import math 
import statistics
import numpy as np 

def expo(mean):
    rand = random.random()
    return -mean*math.log(rand)


def erlang(k, mu):
    result = 0
    for i in range(k):
        result += expo(mu)
    return result 

def binomial(N, prob):
    return np.sum(np.random.binomial(N, prob))


def get_list_of_stats(name, data_list):
    mean = statistics.mean(data_list) 
    stdev = statistics.stdev(data_list)
    # 1.96 for 95% confidence intervall
    sterror = 1.96*stdev / math.sqrt(len(data_list)-1) 
    return [
        name,
        mean,
        "{:.2f}".format(stdev),
        "{:.2f}  -  {:.2f}".format(mean-sterror, mean+sterror),
        min(data_list),
        max(data_list),
    ]


if __name__ == "__main__":
    N = 1000000
    sum = 0
    for i in range(N):
        sum += erlang(3, 5)
    mean = sum/N 
    print("erlang mean = {}".format(mean)) 

    sum = 0
    for i in range(N):
        sum += expo(5)
    mean = sum/N 
    print("expo mean = {}".format(mean)) 
