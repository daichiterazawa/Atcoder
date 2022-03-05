# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:46:06 2022

@author: terad
"""

A,B,C,X = map(int,input().split())

if A >= X:
  print(1)
  
elif B >= X:
  print(C/(B-A))
  
else:
  print(0)