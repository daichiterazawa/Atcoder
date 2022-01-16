# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:54:50 2022

@author: terad
"""

from collections import deque
import sys

a,N = map(int,input().split())
m = 1

#探索木の深さを格納する配列
while m < N:
    m *= 10
d = [-1] * m
    

Q = deque()
Q.append(N)
d[N] = 0

i = 0

while Q and i < 10**6:
    
    x = Q.popleft()
    dc = d[x]
    
    if x == 1:
        print(dc)
        sys.exit()
                
        
    if x % a == 0:
        Q.append(x//a)
        d[x//a] = dc + 1
    
        
    if x >= 10 and x % 10 != 0:
        t,u = str(x%10),str(x//10)
        Q.append(int(t+u))
        d[int(t+u)] = dc + 1

    i += 1    

print(-1)        
    
        
