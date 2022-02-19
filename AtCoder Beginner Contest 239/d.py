# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:36:47 2022

@author: terad
"""

import sys

A,B,C,D = map(int,input().split())
check = [0] * (B-A+1)

def so(num):
    if num <= 3:
        return True
    else:
        for k in range(2,num):
            if num % k == 0:
                return False
            
        return True
            
for i in range(A,B+1):
    for j in range(C,D+1):
        num = i+j
        if so(num) :
            check[i-A] = 1
            break
        
for a in check:
    if a == 0:
        print('Takahashi')
        sys.exit()
    
print('Aoki')
        
        
        