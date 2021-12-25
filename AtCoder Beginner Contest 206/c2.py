# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:43:29 2021

@author: terad
"""

N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = int(N*(N-1)/2)

index = 0
for n in range(N):
    if A[index] != A[n]:
        p = n - index
        ans -= int(p*(p-1)/2)
        index = n
p = N - index
ans -= int(p*(p-1)/2)
    
print(ans)
    