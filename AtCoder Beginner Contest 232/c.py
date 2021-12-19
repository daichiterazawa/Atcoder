# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:19:55 2021

@author: terad
"""
import numpy as np
N,M = map(int,input().split())
check = 0
A_list = np.zeros((N,N))
B_list = np.zeros((N,N))

for m in range(M):
    A,B = map(int,input().split())
    A_list[A-1][B-1] += 1
    A_list[B-1][A-1] += 1
    
for m in range(M):
    A,B = map(int,input().split())
    B_list[A-1][B-1] += 1
    B_list[B-1][A-1] +=1
    
for i in range(N):
    for j in range(N):
        if A_list[i][j] != B_list[i][j]:
            check = 1
print('Yes' if check==0 else 'No')