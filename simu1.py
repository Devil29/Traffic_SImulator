from math import *
from random import random
import plotly.plotly as py
from plotly.graph_objs import *

f=open('inp.txt','r')
g=open('output.txt','w')
previous_angle=0
count=1
path_angle=[]
debug=[]
buff=1000
ran=10
ang=20
data=f.read().split()
path_angle.append(data[0])
debug.append(0)
for i in range(len(data)):
    if(i%buff==0 and i>buff-1):
        previous_angle=0
        for ii in range(ran):
            previous_angle=previous_angle+float(data[i-buff-ii]);
        previous_angle=previous_angle/ran
        if(abs(previous_angle-float(data[i]))>ang):
            count=count+1
            path_angle.append(data[i])
            debug.append(i)
            #print str(abs(previous_angle-float(data[i])))+'\t'+str(previous_angle)+'\t'+str(data[i])+'\t'+str(i)

#write modules for two files

cnt=[]
for i in range(len(debug)):
    cnt.append(i)
trace0= Scatter(x=debug,y=path_angle)
trace1= Scatter(x=cnt,y=path_angle)
data = Data([trace1])
unique_url = py.plot(data, filename = 'basic-line')

g.write("Size of BUFFER   "+str(buff)+'\n')
g.write("Average of this number   "+str(ran)+'\n')
g.write("Max angle Difference  "+str(ang)+'\n')
g.write(str(count)+'\n\n\n\n')
for i in range(len(debug)):
    #g.write(str(debug[i])+" "+str(path_angle[i])+'\n')
    g.write(str(path_angle[i])+'\n')

#close the two file
f.close()
g.close()
        
