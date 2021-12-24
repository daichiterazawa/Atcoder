# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 17:20:06 2021

@author: terad
"""

N,K = map(int,input().split())
a = list(map(int,input().split()))
A = []
ans = []

for i,n in enumerate(a):
    A.append([n,i])
    
A.sort()
okashi,Kdash = divmod(K,N)

for n in range(N):
    if n < Kdash:
        A[n][0] = okashi + 1
    else :
        A[n][0] = okashi

A.sort(key=lambda x: x[1])

for i in range(N):
    print(A[i][0])