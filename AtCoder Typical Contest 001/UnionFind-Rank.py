# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 18:11:56 2021

@author: terad
"""

N,Q = map(int,input().split())
par = [i for i in range(N+1)]
rank = [1] * (N+1)


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
    
    
def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        if rank[x] >= rank[y]:
            par[y] = x
            rank[x] += rank[y]
        else:
            par[x] = y
            rank[y] += rank[x]
            
            
def same(x,y):
    return find(x) == find(y)


for _ in range(Q):
    p,a,b = map(int,input().split())
    
    if p == 0:
        union(a,b)
    else:
        print('Yes' if same(a,b) else 'No')
        
        
