# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:29:29 2021

@author: terad
"""

H,W = map(int,input().split())
A_list = []
check = 0
for _ in range(H):
    A = list(map(int,input().split()))
    A_list.append(A)
    
for i1 in range(H-1):
    for j1 in range(W-1):
        for i2 in range(i1+1,H):
            for j2 in range(j1+1,W):
                if A_list[i1][j1]+A_list[i2][j2] > A_list[i2][j1] + A_list[i1][j2]:
                    check += 1    
                    
print('Yes' if check == 0 else 'No')

                
    
