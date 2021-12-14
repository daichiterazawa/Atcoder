# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:20:10 2021

@author: terad
"""

N,P = map(int,input().split())
a = list(map(int,input().split()))
ans = 0

for n in range(N):
    if a[n] < P:
        ans += 1
        
print(ans)
        
    