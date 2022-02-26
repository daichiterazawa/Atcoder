# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 20:57:42 2022

@author: terad
"""

from collections import Counter

C = Counter([])
Q = int(input())


for i in range(Q):
    x,*n = map(int,input().split())
    if x == 1:
        C[n] += 1
        
    elif x == 2 :
        C