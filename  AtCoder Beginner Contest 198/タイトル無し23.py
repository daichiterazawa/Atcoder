# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 12:12:43 2021

@author: terad
"""

N = int(input())
A = list(map(int,input().split()))
ans = 2147483647
for thr in range(1,N):
    
    a,b = A[:thr],A[thr:]
    aor,bor = 0,0
    
    for x in a:
        aor |= x
    for y in b:
        bor |= y
    
    p = aor ^ bor
    if ans >= p:
        ans = p
        
print(ans)
    
    
    