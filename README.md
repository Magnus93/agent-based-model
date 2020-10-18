#Epidemic CSS and ABM models 

This repo consists of several CSS and ABM files based on the same Conceptual Model.

The ABM models are written in Python and the CCS (`SSD` files) can be run in [StochSD](https://stochsd.sourceforge.io/).

##Set seed to models according to:

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



##Run ABM

Go into any of the files labeled `SIRt` to `2SEI3RtipAed` and run `python collector.py 10000 output.csv`.

This will create and save a csv file containing 10 000 data points.

##CSS (StochSD and StatRes) 

Open StochSD and open the model  desired model.

Open StatRes and and add variable `Epidemic`, `Duration`, `Rt` and `Extinction` to the list

Select seed-of-seeds according to the table above.

Run the model for 10 000 replications and then export the data to a CSV file.

##Get Statistical Results

Get statistical Results by running one of the fore mentioned csv files using:

`python stats.py [model_type] [filename.csv]`

Where `[model_type]` is SIRt, SEIRt, etc.

And `filename.csv` is the desired data file containing 10 000 data points. 









