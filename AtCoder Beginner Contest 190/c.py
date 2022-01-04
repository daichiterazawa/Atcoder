# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:36:22 2022

@author: terad
"""

from itertools import product

N,M = map(int,input().split())
A = [0] * M
B = [0] * M 
ans = 0

for m in range(M):
    A[m],B[m] = map(int,input().split())
    
K = int(input())
CD = []

for k in range(K):
    cd = list(map(int,input().split()))
    CD.append(cd)
    
for t in product(*CD):
    check = 0
    for m in range(M):
        if A[m] in t and B[m] in t:
            check += 1
    if ans < check:
        ans = check
        

print(ans)
    
    


    
    
    
    