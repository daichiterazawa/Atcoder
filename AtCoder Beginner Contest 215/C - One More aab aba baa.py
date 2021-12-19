# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:35:56 2021

@author: terad
"""
from itertools import permutations
 
S,K = map(str,input().split())
S_set = set()
S_list = []

for p in permutations(S):
    S_set.add(''.join(p))

for s in S_set:
    S_list.append(s)
    
S_list.sort()
print(S_list[int(K)-1])

