from math import *
from random import random
f=open('inp.txt','r')
g=open('output.txt','w')
previous_angle=0
count=1
path_angle=[]
data=f.read().split()
path_angle.append(data[0])
for i in range(len(data)):
    if(i%10==0 and i>9):
            previous_angle=(float(data[i-10])+float(data[i-9])+float(data[i-8]))/3
            if(abs(previous_angle-float(data[i]))>8):
                count=count+1;
                path_angle.append(data[i])
    #print str(abs(previous_angle-float(data[i])))+'\t'+str(previous_angle)+'\t'+str(data[i])+'\t'+str(i)
g.write(str(count))
g.write('\n')
g.write(str(path_angle))
f.close()
g.close()
        
