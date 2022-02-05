# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 20:55:28 2022

@author: terad
"""

T = int(input())

for i in range(T):
    a,s = map(int,input().split())
    if s >= 2*a and (s-2*a & a == 0):
        print('Yes')
    
    else:
        print('No')
