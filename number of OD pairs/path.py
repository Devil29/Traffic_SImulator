from math import *
from numpy import *

total=8
f=open('path.txt','r')
matrix=zeros((total,total))
for line in f:
    nodes=line.split(' ')
    matrix[int(nodes[0])-1][int(nodes[1])-1]=1
    matrix[int(nodes[1])-1][int(nodes[0])-1]=1
f.close()


