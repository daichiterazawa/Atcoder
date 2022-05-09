# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:20:39 2022

@author: terad
"""


N,Q = map(int,input().split())
P = [i for i in range(N+1)]
L = [i for i in range(N+1)]

for _ in range(Q):
    x = int(input())
    
    #ここでxの配列番号を確認
    y1 = L[x]
    
    if y1 != N:
        y2 = y1+1
        L[x],L[P[y2]] = L[P[y2]],L[x]
        P[y1],P[y2] = P[y2],P[y1]
        
    else:
        y2 = y1-1
        L[x],L[P[y2]] = L[P[y2]],L[x]
        P[y1],P[y2] = P[y2],P[y1]
        
for p in P[1:]:
    print(p,end=' ')
        
        
    