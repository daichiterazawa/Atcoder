# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:57:08 2022

@author: terad
"""
from collections import deque


N = int(input())
A =list(map(int,input().split()))
d = deque([[A[0],1]])
k = 0

print(1)
for i in range(1,N):
    p = A[i]
    if i - k > 0:
        if p == d[-1][0]:
            d[-1][1] += 1
            
        else:
            d.append([p,1])
    else:
        d.append([p,1])
        
    if d[-1][0] == d[-1][1]:
        k += d[-1][0]
        d.pop()
    
    print(i-k+1)



    
