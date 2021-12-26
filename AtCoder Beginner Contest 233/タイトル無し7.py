# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 23:56:56 2021

@author: terad
"""


N,X = map(int,input().split())
L = []
A = []
for _ in range(N):
    l,*a = map(int,input().split())
    L.append(l)
    A.append(a)
 
B = A[0]
C = []
ans = 0
for n in range(1,N-1):
    for a in  A[n]:
        for b in B:
            if a*b <= X:
                C.append(a*b)
    B = C
 
for a in A[N-1]:
    for b in B:
        if a*b == X:
            ans += 1
            
print(ans)
    

    
    