# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:54:50 2022

@author: terad
"""

from collections import deque
import sys

a,N = map(int,input().split())

Q = deque()
Q.append(N)
ans = 0

while Q:
    ans += 1
    x = Q.popleft()
    
    if x == 1:
        for i in range(ans):
            if ans < 2**i:
                print(i)
                sys.exit()
                
        sys.exit()
    if x % a == 0:
        Q.append(x//a)
    else :
        Q.append(-1)
        
    if x >= 10 and x % 10 != 0:
        t,u = str(x%10),str(x//10)
        Q.append(int(t+u))
    else :
        Q.append(-1)
        
    
    

print(-1)        
    
        
