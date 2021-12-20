# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:54:52 2021

@author: terad
"""

A,B = map(int,input().split())
 
for i in range(256):
  if A^i == B:
    print(i)
    break