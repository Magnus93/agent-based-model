import random
import math 


def expo(mean):
    rand = random.random()
    return -mean*math.log(rand)


def erlang(order, mean):
    result = 0
    for i in range(order):
        result += expo(mean/order) 
    return result 
     