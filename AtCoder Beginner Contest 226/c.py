# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 20:48:07 2022

@author: terad
"""
from collections import deque

N =  int(input())
T = [0]
K = [0]
A = [0]


for i in range(N):
    t,k,*a = map(int,input().split())
    T.append(t)
    K.append(k)
    A.append(a)
    
#BFS
d = deque()
d.append(N)
waza = [True]*(N+1)
ans = T[N]

while d :
    x = d.popleft()
    Ad = A[x]
    for ad in Ad:
        if waza[ad]:
            if ad != 1:
                d.append(ad)
                
            ans += T[ad]
            waza[ad] = False

print(ans)
            
    
    
    
    
    
    

    