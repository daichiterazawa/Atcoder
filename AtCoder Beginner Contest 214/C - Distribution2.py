# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 20:42:27 2021

@author: terad
"""

N = int(input())
ans = [0] * N
S = list(map(int,input().split()))
T = list(map(int,input().split()))

for n in range(2*N):
    T[(n+1)%N] = min(T[(n+1)%N],T[n%N]+S[n%N])
    
[print(ans) for ans in T]
