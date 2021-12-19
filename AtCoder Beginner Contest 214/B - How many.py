# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:57:14 2021

@author: terad
"""

S,T = map(int,input().split())
check = 0
 
for a in range(101):
    for b in range(101):
        for c in range(101):
            if a+b+c <= S and a*b*c <= T:
                check += 1
                
print(check)