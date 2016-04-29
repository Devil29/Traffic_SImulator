from math import *
from collections import defaultdict


Number_of_nodes=12
Matrix = defaultdict(list)
Output = defaultdict(list)

f=open('road_angles.txt','r')
for line in f:
    data=line.split()
    if(len(data)>2):
        from_node=data[0]
        to_node=data[1]
        turn_angle=data[2]
        Matrix[int(float(turn_angle))].append(from_node + ' ' + to_node);
        print  from_node, to_node, turn_angle

f=open('road_angles_turnings.txt','r')
i=0
error_range=3
nodes=0
first_node=0
second_node=0
previous_nodes=0
previous_first_node=0
previous_second_node=0
for line in f:
    if(len(line)<2):
        break;
    turn=int(float(line))
    if(i==0):
        Output[i]=Matrix[turn]
    else:
        for ii in range(0,2*error_range+1):
            turning=turn-error_range+ii
            print turning
            for edge in Matrix[turning]:
                nodes=edge.split(' ');
                first_node=nodes[-2];
                second_node=nodes[-1];
                for previous_edge in Output[i-1]:
                    previous_nodes=previous_edge.split(' ');
                    previous_first_node=previous_nodes[-2];
                    previous_second_node=previous_nodes[-1];
                    if(first_node==previous_second_node):
                        Output[i].append(previous_edge+':'+edge);
    if(Output[i] is None):
        print "No such path"
        break;
    i+=1;
print "Path is =>  ",Output[i-1]
    
    
        
