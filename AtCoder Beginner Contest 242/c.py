# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:47:02 2022

@author: terad
"""

N = int(input())
num = [0] + [1 for i in range(1,10)] + [0]

for i in range(N-1):
    a = [0] * 11
    for j in range(9):
        a[j+1] = (num[j] + num[j+1] +num[j+2]) % 998244353
    
    num = a
    
    
print(sum(num)%998244353)
    