from math import *
from numpy import *
f=open('path.txt','r')
total=8;
matrix=zeros((total,total))
for line in f:
    edge=line.split(' ')
    print edge
    matrix[int(edge[0])-1][int(edge[1])-1]=1
    matrix[int(edge[1])-1][int(edge[0])-1]=1
print matrix
for i in range(8):
    for j in range(8):
        if(matrix[i][j]==1):
            #Apply BFS


