# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:41:18 2021

@author: terad
"""

N = int(input())
A = list(map(int,input().split()))
ans = 0
for a in range(N):
    ans += A[a] - 10 if A[a] >= 10 else 0
print(ans)