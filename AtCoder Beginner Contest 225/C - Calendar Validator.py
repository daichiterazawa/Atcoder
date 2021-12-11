# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:17:56 2021

@author: terad
"""
import numpy as np
N,M = map(int,input().split())
check = 0
B = np.array(list(map(int,input().split())))
if B[M-1] > (B[0]+(7-B[0]%7)%7) :
    check = 1
    
for i in range(M):
    if i != B[i]-B[0]:
        check = 1

for _ in range(N-1):
    B_new = np.array(list(map(int,input().split())))
    if sum(B_new - (B+7)) != 0:
        check = 1
    B = B_new
        
print('Yes' if check==0 else 'No')
        
    
    
    
    

