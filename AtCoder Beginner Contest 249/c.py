# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:56:22 2022

@author: terad
"""


import itertools
from collections import Counter

N,K = map(int,input().split())
S = []
ans = 0

for _ in range(N):
    S.append(input())
    
for i in range(1,N+1):
    combi = itertools.combinations(S,i)
    for s in combi:
        count =Counter(''.join(list(s)))
             
        check = 0
        for c in count.values():
            if c == K:
                check += 1
            
            if check > ans:
                ans = check

print(ans)