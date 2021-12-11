# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:23:19 2021

@author: terad
"""

S,T = map(int,input().split())
check = 0

for a in range(S+1):
    for b in range(S+1):
        for c in range(S+1):
            if a+b+c <= S and a*b*c <= T:
                check += 1
                
print(check)