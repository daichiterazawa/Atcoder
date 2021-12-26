# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 12:58:38 2021

@author: terad
"""

N,Q = map(int,input().split())
par = [i for i in range(N+1)]

#親を探すプログラム
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
        par[x] = y


def same(x,y):
    return find(x) == find(y)
    
    
for _ in range(Q):
    p,a,b = map(int,input().split())
    #連結クエリの場合
    if p == 0:
        union(a,b)
    #判定クエリの場合
    else:
        if same(a,b):
            print('Yes')
        else:
            print('No')
            
            
        
        