# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:36:47 2022

@author: terad
"""

N,Q = map(int,input().split())
X = list(map(int,input().split()))
Y = [[1,1]] + [[-1,i] for i in range(2,N+1)]

