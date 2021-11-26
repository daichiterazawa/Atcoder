# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 21:22:40 2021

@author: terad
"""

N, K, A = map(int, input().split())

K = K % N
num = A + K - 1
ans = num % N

print(ans if ans != 0 else N)
    