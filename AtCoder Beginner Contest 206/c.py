# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:22:44 2021

@author: terad
"""
N = int(input())
A = list(map(int,input().split()))
ans = 0

for i in range(N-1):
    for j in range(i,N):
        if A[i] != A[j]:
            ans += 1
            
print(ans)