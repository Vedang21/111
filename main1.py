import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import csv
df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)
sd=statistics.stdev(data)
print("mean is:-",mean)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
mean=statistics.mean(mean_list)
print("mean of sampling disterbution",mean)
first_sd_start,first_sd_end=mean-sd,mean+sd

fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="SD1 START"))