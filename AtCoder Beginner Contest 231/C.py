# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:19:58 2021

@author: terad
"""
N,Q = map(int,input().split())
A = list(map(int,input().split()))
for _ in range(Q):
    x = int(input())
    print(len([s for s in A if s >= x]))
