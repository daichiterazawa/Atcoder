# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:10:32 2021

@author: terad
"""

N = int(input())
A = list(map(int,input().split()))
B = []
for i,a in enumerate(A):
    B.append([a,i])
B.sort()
print(B[-2][1] + 1)