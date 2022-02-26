# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 20:57:41 2022

@author: terad
"""
import sys

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(M):
    a = B[i]
    for j in range(N):
        if a == A[j]:
            A[j] = 0
            break
        if j == N-1:
            print('No')
            sys.exit()
            
print('Yes')