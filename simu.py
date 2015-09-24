from math import *
from random import random
f=open('inp.txt')
previous_angle=0
count=0
data=f.read().split()
for i in range(len(data)):
    if(i%10==0 and i>9):
            previous_angle=(float(data[i-10])+float(data[i-9])+float(data[i-8]))/3
            if(abs(previous_angle-float(data[i]))>8):
                count=count+1;
    #print str(abs(previous_angle-float(data[i])))+'\t'+str(previous_angle)+'\t'+str(data[i])+'\t'+str(i)
print count;
        
