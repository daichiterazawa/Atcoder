# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:52:04 2022

@author: terad
"""
import copy
from itertools import permutations

N = int(input())
A = []
check = 0
ans = 0

for i in range(2*N-1):
    a = list(map(int,input().split()))
    A.append([0]*(i+1) + a)

for x in permutations(range(2*N)):
    check = 0
    for n in range(N):
        if x[2*n] < x[2*n+1]:
            check ^= A[x[2*n]][x[2*n+1]]
        else :
            break
    if ans < check:
        ans = check

print(ans)     
    