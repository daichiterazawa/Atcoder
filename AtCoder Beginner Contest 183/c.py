# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 20:17:19 2022

@author: terad
"""

from itertools import permutations

N,K = map(int,input().split())
T = [[0] * N for _ in range(N)]
ans = 0

for i in range(N):
    T[i] = list(map(int,input().split()))
    
for a in permutations(range(1,N)):
    check = 0
    
    check += T[0][a[0]]
    
    for i in range(N-2):
        check += T[a[i]][a[i+1]]
        
    check += T[a[N-2]][0]
    
    
    if check == K :
        ans += 1
        
print(ans)
    
    
