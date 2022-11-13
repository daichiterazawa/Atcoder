# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:52:48 2022

@author: terad
"""
N,M = map(int,input().split())
ans = [[] for i in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    ans[a-1].append(b)
    ans[b-1].append(a)
    
for A in ans:
    print(len(A),end=' ')
    A.sort()
    for a in A:
        print(a,end=" ")
    print('\n',end='')
        
    