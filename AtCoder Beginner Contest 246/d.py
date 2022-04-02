# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 20:45:47 2022

@author: terad
"""
import sys

N = int(input())
n_low = 0
n_high = 0
ans = 0

for i in range(10**10):
    x = i ** 3 * 4
    if x == N :
        print(x)
        sys.exit()
        
    if x > N :
        n_low = i 
        break
for i in range(10 ** 10):
    y = i ** 3
    if y == N:
        print(y)
        sys.exit()
        
    if y > N :
        n_high = i
        break
    
    
d = 10 ** 20
for i in range(n_low,n_high):
    if i % 2 == 0:
        
    j_low
    num = i**3 + i**2 * j + i * j**2 + j**3
    if num - N < 0:
        break
    if d > num - N :
        d = num - N
        ans = num
            
print(ans)
        
    