# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 20:53:09 2022

@author: terad
"""

N,L,W = map(int,input().split())
A = [0] + list(map(int,input().split())) + [L]
x = 0
ans = 0

   
for i in range(N+1):
    if A[i+1] > A[i] + W:
        ans += int((A[i+1] - A[i] - W - 0.1)//W)

print(ans)

    