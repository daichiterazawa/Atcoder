# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:24:50 2022

@author: terad
"""

N = int(input())
ans = 0
 
for i in range(N):
  a,b = map(int,input().split())
  ans += (a+b)*(b-a+1)//2
  
print(ans)