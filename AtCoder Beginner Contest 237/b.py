# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:55:53 2022

@author: terad
"""
H,W = map(int,input().split())

A = [[0] * W for _ in range(H) ]

for n in range(H):
    A[n] = list(map(int,input().split()))
    
for i in range(W):
    for j in range(H):
        print(A[j][i],end=' ')
    print('\n')