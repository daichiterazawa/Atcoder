# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:31:35 2022

@author: terad
"""

A = list(input())
B = int(input())

if B % 2 == 0:
    B = list(str(B//2))
else:
    B = list(str(B//2)) + ['5']
    
 
print(''.join(A+B))