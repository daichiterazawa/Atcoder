# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:34:27 2021

@author: terad
"""

a = list(input())
d = {'0':0, '1':1, '6':9, '9':6, '8':8}
 
for i in reversed(a):
  print(d[i],end='')