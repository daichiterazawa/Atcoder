# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 15:04:44 2022

@author: terad
"""
from itertools import accumulate
from collections import Counter

N,K = map(int,input().split())
A = list(map(int,input().split()))
B = accumulate(A)
C = Counter()
ans = 0

#r=lの場合を数えるためC=0を追加
C[0] += 1

for b in B:
    a = b - K 
    ans += C[a]
    C[b] += 1
    
print(ans)

