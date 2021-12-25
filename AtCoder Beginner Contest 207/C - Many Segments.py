# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 13:43:02 2021

@author: terad
"""

N = int(input())
ranges = []
ans = 0
for _ in range(N):
    t,l,r = map(int,input().split())
    
    
    if t == 1:
        ranges.append([l,r])
    elif t == 2:
        ranges.append([l,r-0.01])
    elif t == 3:
        ranges.append([l+0.01,r])
    else:
        ranges.append([l+0.01,r-0.01])
        
for i in range(N-1):
    for j in range(i+1,N):
        if ranges[i][0] <= ranges[j][1] and ranges[i][1] >= ranges[j][0]:
            ans += 1
            
print(ans)
            

            
        
            
        