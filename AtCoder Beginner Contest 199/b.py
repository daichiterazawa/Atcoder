# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 22:54:47 2022

@author: terad
"""

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a,b = max(A),min(B)

print(b-a+1 if b >= a else 0)