# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 14:47:18 2021

@author: terad
"""

N = int(input())
S = list(map(int,input().split()))
S_list = []
check = 0
for a in range(1,144):
    for b in range(1,144):
        S_list.append(4*a*b+3*a+3*b)
        
for n in range(N):
    if S[n] not in S_list:
        check += 1
        
print(check)
        