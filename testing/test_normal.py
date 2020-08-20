import random 
import matplotlib.pyplot as plt

values = []
bins = 30


for i in range(100000):
    values.append(max(0, random.normalvariate(1, 0.25)))

plt.hist(values, bins)
plt.show() 

