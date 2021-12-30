# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:46:22 2021

@author: terad
"""

A = list(map(int,input().split()))
A.sort()

print('Yes' if A[2]-A[1] == A[1]-A[0] else 'No')
