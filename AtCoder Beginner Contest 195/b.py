# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:34:30 2022

@author: terad
"""

A,B,W = map(int,input().split())

nmax,nmin = -1,-1

for i in range(1,1000001):
    if A * i <= W * 1000 <= B * i:
        if nmin == -1:
            nmin = i
        
        nmax = i
        
if nmax == -1 and nmin == -1:
    print('UNSATISFIABLE')
else:
    print(nmin,nmax)