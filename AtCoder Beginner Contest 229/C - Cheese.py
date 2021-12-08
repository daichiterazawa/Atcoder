# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 22:08:00 2021

@author: terad
"""
import numpy as np

N,W = map(int, input().split())
A_list = []
B_list = []

for i in range(N):
    A,B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)
    
A_np = np.array(A_list)
B_np = np.array(B_list)

A_sorted = np.sort(A_np)[::-1]
B_sorted = B_np[np.argsort(A_np)[::-1]]

mount = 0
oisi = 0
i = 0

if sum(B_sorted) <= W:
    oisi = sum(A_sorted * B_sorted)
    
else: 
    while mount < W:
        
        if mount + B_sorted[i] <= W:
            mount = mount + B_sorted[i]
            oisi = oisi + A_sorted[i] * B_sorted[i]
            
        else:
            
            oisi = oisi + A_sorted[i] * (W-mount)
            mount = W
            
        i = i+1
    
print(oisi)
    
    
    
    