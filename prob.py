import random
import math 
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
