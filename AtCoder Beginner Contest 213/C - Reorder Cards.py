# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:19:05 2021

@author: terad
"""
H,W,N = map(int,input().split())
A,B = [],[]

for _ in range(N):
    ab = list(map(int,input().split()))
    A.append(ab[0])
    B.append(ab[1])
    

Cdict = {a : i+1 for i,a in enumerate(sorted(list(set(A))))}
Ddict = {b : j+1 for j,b in enumerate(sorted(list(set(B))))}

[print(Cdict[A[i]],Ddict[B[i]]) for i in range(N)]
