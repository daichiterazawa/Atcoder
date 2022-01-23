# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:51:56 2022

@author: terad
"""

from collections import Counter
N,M = map(int,input().split())

A = input().split()
B = input().split()

BC = Counter(B)

for n in A:
    if BC[n] == 1:
        print('Yes')
    else:
        print('No')