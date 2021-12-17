# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 13:50:39 2021

@author: terad
"""

K = int(input())
A,B = map(str,input().split())

 
A10 = int(A, base=K)
B10 = int(B, base=K)
 
print(A10*B10)