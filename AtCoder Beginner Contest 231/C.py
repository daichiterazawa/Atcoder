# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:19:58 2021

@author: terad
"""
from bisect import insort
N,Q = map(int,input().split())
A = list(map(int,input().split())).sort(reverse = True)

for _ in range(Q):
    x = int(input())
    

