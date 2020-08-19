from prob import *
import pandas as pd 

sums = { 
    "uniform": 0, 
    "expo":    0,
    "1erlang": 0, 
    "2erlang": 0,
    "3erlang": 0,
    "4erlang": 0 
}


N = 10000
for i in range(N):
    sums["uniform"] += random.random()
    sums["expo"] += expo(5)
    sums["1erlang"] += erlang(1, 15)
    sums["2erlang"] += erlang(2, 7.5)
    sums["3erlang"] += erlang(3, 5)
    sums["4erlang"] += erlang(4, 3.75)

print(N)
for r in sums:
    print("{}: \t{}".format(r, sums[r]/N))

