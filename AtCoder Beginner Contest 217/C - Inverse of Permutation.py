# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:29:58 2021

@author: terad
"""
import copy 

N = int(input())
P = list(map(int,input().split()))
Q = copy.deepcopy(P)

for i,j in enumerate(P):
    Q[j-1] = i+1
    
for n in range(N):
    print(Q[n],end=' ')
