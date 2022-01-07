# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 20:45:01 2022

@author: terad
"""
from itertools import combinations
import sys

N = list(input())
l = []
ans = -1
#各桁の値をリストに格納
for i in N:
    l.append(int(i))
    
for i in range(len(l)):
    for t in combinations(l,len(l)-i):
        if sum(t) % 3 == 0:
            print(i)
            sys.exit()
print(-1)
    
    