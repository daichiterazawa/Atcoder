# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 10:45:47 2021

@author: terad
"""

N = int(input())
S = list(input())
Q = int(input())

for i in range(Q):
    t,a,b = map(int,input().split())
    if t == 1:
        tmp = S[a-1]
        S[a-1] = S[b-1]
        S[b-1] = tmp
    else:
        tmp = S[:N]
        S[:N] = S[N:]
        S[N:] = tmp
for s in S:
    print(s,end='')

        