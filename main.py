import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import csv
df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
#fig=ff.create_distplot([data],["Math Score"],show_hist=False)
#fig.show()

#mean=statistics.mean(data)
sd=statistics.stdev(data)
#print("mean is:-",mean)
#print("sd is:-",sd)

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
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

print("sd1",first_sd_start,first_sd_end)
print("sd2",second_sd_start,second_sd_end)
print("sd3",third_sd_start,third_sd_end)

fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="SD1 START"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="SD1 END"))
fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode="lines",name="SD2 START"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="SD2 END"))
fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.17],mode="lines",name="SD3 START"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="SD3 END"))
fig.show()