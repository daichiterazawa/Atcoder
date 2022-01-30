# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:55:53 2022

@author: terad
"""

N = int(input())
S = list(input())
numL = []
numR = []

for i,s in enumerate(S):
    if s == 'L':
        numR.append(i)
    else:
        numL.append(i)

if S[-1] == 'L':
    numL.append(N)
else:
    numR.append(N)
     
for l in numL:
    print(l,end=' ')

    
for r in numR[::-1]:
    print(r,end=' ')
        
    
    
    