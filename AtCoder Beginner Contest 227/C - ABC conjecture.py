# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:05:21 2021

@author: terad
"""

N = int(input())
check = 0

for a in range(1,N+1):
    if a**3 > N:
        break
    for b in range(a,N+1):
        if a*b**2 > N:
            break
        check += N//a//b-b+1

print(check)
                