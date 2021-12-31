# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:37:55 2021

@author: terad
"""

n,k = map(int,input().split())
 
for _ in range(k):
    if n%200 != 0:
        n = int(n*1000 + 200)
    else:
        n = int(n/200)
        
print(n)