# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:59:48 2021

@author: terad
"""

A,B,C = map(int,input().split())
ans = -1
 
for i in range(A,B+1):
  if i % C == 0 :
    ans = i
    break
print(ans)