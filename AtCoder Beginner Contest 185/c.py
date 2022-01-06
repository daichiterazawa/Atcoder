# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 22:43:40 2022

@author: terad
"""
from math import factorial

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

L = int(input())
X = L - 12
ans = comb(X + 11, 11)
print(ans)