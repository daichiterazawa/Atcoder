# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:21:24 2021

@author: terad
"""

S1 = input()
S2 = input()
S3 = input()
T = list(input())

D = {'1':S1, '2':S2, '3':S3}

[print(D[i],end="") for i in T]