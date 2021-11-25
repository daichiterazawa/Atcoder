# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 17:56:46 2021

@author: terad
"""

N, X = map(int, input().split())
A = [-1] + list(map(int,input().split()))
flag = [False] * (N + 1)
flag[X] = True
now = X
while not flag[A[now]]:
    now = A[now]
    flag[now] = True
    
print(flag.count(True))

