import time 
import random 
import math 
import numpy as np 

interations = 10000
size = 1000

lst = []
for i in range(size):
    lst.append({"value": 0}) 


start_serial = time.time()
for i in range(interations):
    for i in range(size):
        lst[0]["value"] = -5*math.log(random.random())
serial_time = time.time() - start_serial 

print("serial_time \t{}".format(serial_time)) 

values = np.array([]) 

for i in range(size):
    np.append(values, [0])



start_np = time.time()
for i in range(interations):
    values = -5*np.log(np.random.random([size])) 
np_time = time.time() - start_np

print("np_time \t{}".format(np_time)) 