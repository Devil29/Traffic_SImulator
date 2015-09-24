from math import *
from random import random
r=open('input.txt','r')
f=open('inp.txt','w')
t=int(r.readline())
for i in range(t):
    readings=r.readline().split(' ',1)
    b,c=int(readings[0]),int(readings[1])
    for i in range(b*10):   
        f.write(str(c+(random()*2)-1)+"\n")
f.close()
r.close()
