# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:19:58 2021

@author: terad
"""
import numpy as np
N,M = map(int,input().split())
data_set = set()
hito = np.zeros(N)
check = 0
for _ in range(M):
    data_set.add(tuple(map(int,input().split())))
   
for A,B in data_set:
    
    if hito[A-1] < 2 and hito[B-1] < 2:
        hito[A-1] += 1
        hito[B-1] += 1
    else :
        check = 1
        break
    
print('Yes' if check==0 else 'No')
    

    
