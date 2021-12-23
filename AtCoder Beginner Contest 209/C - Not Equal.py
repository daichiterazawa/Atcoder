# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:02:16 2021

@author: terad
"""

N = int(input())
C = list(map(int,input().split()))
C.sort()
ans = 1
for i in range(N):
    ans *= (C[i]-i)
    if ans <= 0:
        ans = 0
        break
    ans = ans %(10**9+7)
print(ans)