# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 16:13:33 2021

@author: terad
"""

N,K = map(int,input().split())
c = list(map(int,input().split()))
max_num = 0

for s in range(N-K+1):
    num = len(set(c[s:s+K]))
    if num >= max_num:
        max_num = num
print(max_num)