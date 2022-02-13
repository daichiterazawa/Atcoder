# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:24:58 2022

@author: terad
"""

import sys

N = int(input())
XY = []
check = []

for i in range(N):
    xy = list(map(int,input().split()))
    XY.append(xy)
    
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j != k:
                if (XY[i][0]-XY[j][0]) != 0:
                    p = (XY[i][1]-XY[j][1])/(XY[i][0]-XY[j][0])
                else:
                    p = 1000000000
                
                if (XY[j][0]-XY[k][0]) != 0:
                    q = (XY[j][1]-XY[k][1])/(XY[j][0]-XY[k][0])
                else:
                    q = 1000000000
            else:
                continue
            
            if p == q :
                print('Yes')
                sys.exit()
 
print('No')