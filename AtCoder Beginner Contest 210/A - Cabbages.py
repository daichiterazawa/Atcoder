# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 16:01:30 2021

@author: terad
"""

N,A,X,Y = map(int,input().split())
if N > A:
  print(Y*N + (X-Y)*A)
else:
  print(X*N)