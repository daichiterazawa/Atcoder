# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 20:45:47 2022

@author: terad
"""

N,K,X = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
memo = 0
for i in range(len(A)):
    n = min(K,A[i] // X)
    m = A[i] - X*n
    A[i] = m
    K -= n
    
A.sort()
A.reverse()
ans = sum(A[K:])    

print(ans)
