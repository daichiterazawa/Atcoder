# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:46:49 2021

@author: terad
"""
import numpy as np

N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())

for i in range(P,Q+1):
    for j in range(R,S+1):
        k = i - A 
        if k == j - B and max([1-A,1-B]) <= k and min([N-A,N-B]) >= k:
            print("#",end="")
            
        elif k == B - j and max([1-A,B-N]) <= k and min([N-A,B-1]) >= k:
            print("#",end="")
            
        else:
            print(".",end="")
    print("\n")
            
            
    



