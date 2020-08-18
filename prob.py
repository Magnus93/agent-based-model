import random
import math 
import numpy as np 

def expo(mean):
    rand = random.random()
    return -mean*math.log(rand)


def erlang(order, mean):
    result = 0
    for i in range(order):
        result += expo(mean/order) 
    return result 

def binomial(N, prob):
    return np.sum(np.random.binomial(N, prob))