# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:15:23 2021

@author: terad
"""

N = int(input())
money = 0
for ans in range(1,10**10):
  money += ans
  if money >= N :
    break
print(ans)