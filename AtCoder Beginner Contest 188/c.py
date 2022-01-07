# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 21:53:32 2022

@author: terad
"""

N = int(input())
A = list(map(int,input().split()))

a = max(A[:2**(N-1)])
b = max(A[2**(N-1):])

print(A.index(min(a,b)) + 1)