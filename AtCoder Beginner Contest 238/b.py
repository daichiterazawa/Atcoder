# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 20:55:14 2022

@author: terad
"""
import itertools

N = int(input())
A = list(map(int,input().split()))
A = list(itertools.accumulate(A))
B = [0]


for a in A:
    B.append(a%360)
    
B.sort()

ans = 360-B[-1] 
for i in range(len(B)-1):
    x = B[i+1] - B[i]
    if x > ans:
        ans = x
        
print(ans)
    
    


    
    