# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 18:30:14 2021

@author: terad
"""

a,b,c = map(int,input().split())
if a == b:
  print(c)
elif b == c :
  print(a)
elif a == c:
  print(b)
else:
  print(0)