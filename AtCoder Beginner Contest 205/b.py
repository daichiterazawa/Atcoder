# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:17:34 2021

@author: terad
"""

N = int(input())
target = [i+1 for i in range(N)]
A = list(map(int,input().split()))
A.sort()

if A == target:
    print('Yes')
else:
    print('No')