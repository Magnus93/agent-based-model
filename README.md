#agent-based-seir

Agent Based SEIR simulation model made in python. The model is used to be compared with a StochSD model. 



# Set seed to models according to:

| model        | SEED  |
| ------------ | ----- |
| SIR          | NONE  |
| SIRt         | 1232  |
| SEIRt        | 1233  |
| SEI3Rt       | 1234  |
| 2SEI3Rt      | 1235  |
| 2SEI3Rti     | 1236  |
| 2SEI3Rtip    | 1237  |
| 2SEI3RtipA   | 1238  |
| 2SEI3RtipAe  | 1239  |
| 2SEI3RtipAed | 12310 |



#Compare ABM and CSS model

##ABM

Run: `python collector.py 1000`.

1000 specifies the number of replications.

This will generate a CSV-file called `abm-density-1000reps-20bins.csv`.

##CSS (StochSD and StatRes) 

Open StochSD and open the model  `...` 

Open StatRes and and add variable `Epidemic` to the list run the model for 1000 replications and then export the result to CSV.

Rename the exported file to `css-data.csv`  for clarity and then run the command: 

`python convert-epidemic-data-to-cdf.py css-data.csv` 

This will convert the epidemic data to the file `css-density-1000reps-20bins.csv` 



## Compare ABM CDF and CSS CDF

run the script: 

`python .\get-p-p-plot.py abm-density-20reps-20bins.csv css-density-1000reps-20bins.csv`

This will merge the the files into one CSV-file. Here the file can be opened in a speadsheet program of your choosing to compare the two CSV-files in a p-p diagram. 







