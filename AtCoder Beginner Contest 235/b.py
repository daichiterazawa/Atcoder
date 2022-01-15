# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:54:24 2022

@author: terad
"""
import sys
N = int(input())
H = list(map(int,input().split()))
ans = 0

for h in H:
    if h > ans:
        ans = h
        
    else:
        print(ans)
        sys.exit()
        
print(ans)
