# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:51:55 2022

@author: terad
"""

N = int(input())
A = map(int,input().split())
B = sum(A)

print(N*(N+1)*2 - B)