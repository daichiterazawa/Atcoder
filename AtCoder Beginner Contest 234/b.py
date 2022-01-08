# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:45:04 2022

@author: terad
"""
import math

N = int(input())
P = []
ans = 0
for n in range(N):
    x,y = map(int,input().split())
    P.append(x,y)

for i in P:
    for j in P:
        d = math.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2)
        if d > ans:
            ans = d
            
print(ans)
    
        