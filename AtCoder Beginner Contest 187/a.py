# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 21:18:44 2022

@author: terad
"""

A,B = map(str,input().split())
x,y = 0,0
for a in list(A):
  x += int(a)
  
for b in list(B):
  y += int(b)
  
print(max(x,y))