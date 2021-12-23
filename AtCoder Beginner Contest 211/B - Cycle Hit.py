# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:03:51 2021

@author: terad
"""

S = set()
for _ in range(4):
  a = input()
  S.add(a)
  
print('Yes' if S == {'H','2B','3B','HR'} else 'No')