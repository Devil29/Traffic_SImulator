from math import *
from random import random
import plotly.plotly as py
from plotly.graph_objs import *

f=open('inp.txt','r')
data=f.read().split()
cnt=[]
path_angle=[]
for i in range(len(data)):
    cnt.append(i)
    path_angle.append(float(data[i]));
trace1= Scatter(x=cnt,y=path_angle)
data = Data([trace1])
unique_url = py.plot(data, filename = 'basic-line')
f.close()

        
