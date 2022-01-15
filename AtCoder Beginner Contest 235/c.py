# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:54:50 2022

@author: terad
"""

#辞書型にリストを入れる
N,Q = map(int,input().split())
A = list(map(int,input().split()))
d = {}

for i,a in enumerate(A):
    if a in d:
        d[a].append(i+1)
    else:
        d[a] = [i+1]
        
for q in range(Q):
    x,k = map(int,input().split())
    if x in d and len(d[x]) >= k:
        print(d[x][k-1])
    else:
        print(-1)
