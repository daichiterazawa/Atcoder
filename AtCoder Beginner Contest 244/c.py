# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:44:20 2022

@author: terad
"""

import sys 

N = int(input())
print(1,flush=True)

A = [1] + [0] * (2*N)

for i in range(N):
    b = int(input())
    A[b-1] = 1
    for j,a in enumerate(A):
        if a == 0:
            A[j] = 1
            print(j+1,flush=True)
            
            break

c  = int(input())
sys.exit()
        