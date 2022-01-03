# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:26:11 2022

@author: terad
"""
import numpy as np

N = int(input())
s = set()

for a in range(2,int(np.sqrt(N))+1):
    for b in range(2,N):
        if a**b > N:
            break
        else:
            s.add(a**b)
            
print(N - len(s))
        
        
        