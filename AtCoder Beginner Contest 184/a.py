# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 23:10:18 2022

@author: terad
"""

A = [[0] * 2 for _ in range(2)]

for i in range(2):
    A[i] = list(map(int,input().split()))
    
print(A[0][0]*A[1][1] - A[0][1]*A[1][0])
    
    