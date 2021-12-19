# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:49:24 2021

@author: terad
"""

N = int(input())
k = 0

while N != 1:
  N = N / 2
  k += 1
  
print(k)