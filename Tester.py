from math import *
from random import random
r=open('input.txt','r')
f=open('inp.txt','w')
t=int(r.readline())
previous_angle=0
for ii in range(t):
    readings=r.readline().split(' ')
    b,c,d=int(readings[0]),int(readings[1]),int(readings[2])
    for i in range(b*10):
        if(d==0):
            #f.write(str(c+(random()*2)-1)+"    "+str(previous_angle)+"\n")
            f.write(str(c+(random()*2)-1)+"\n")
            previous_angle=c
        elif(d==1 and ii==0):
            previous_angle=c
        else:
            f.write(str(previous_angle+(random()*2)-1+(c*i/(b*10)))+"\n")
            #f.write(str(previous_angle+(random()*2)-1+(c*i/(b*10)))+"    "+str(previous_angle)+" HERE---\n")
f.close()
r.close()
