# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:02:44 2022

@author: terad
"""

n = int(input())
R = list(map(int,input().split()))
C = list(map(int,input().split()))
q = int(input())

for i in range(q):
    r,c = map(int,input().split())
    
    if R[r-1] + C[c-1] > n:
        print('#',end='')
    else:
        print('.',end='')
        
