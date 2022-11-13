# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:52:49 2022

@author: terad
"""

S = list(input())
ans = -1
for i,s in enumerate(S):
    if s == 'a':
        ans = i+1
        
print(ans)