from prob import *
import pandas as pd 


table = pd.DataFrame(columns=["unifrom", "expo", "erlang-2", "erlang-3", "erlang-4", "tri"])

N = 100000
for i in range(N):
    if i % 1000 == 0:
        print(i) 
    table.loc[len(table)] = [ 
        random.random(),
        expo(5),
        erlang(2, 5),
        erlang(3, 5),
        erlang(4, 5),
        random.triangular(2, 7, 5)
    ] 

table.to_csv("random-distributions.csv")
