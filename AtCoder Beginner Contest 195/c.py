# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 11:22:16 2022

@author: terad
"""

N = int(input())
ans = 0

for i in range(6):
    if N >= 10**(3*(i+1))-1:
        num = N - (10**(3*(i+1))-1)
        ans += num 
    else:
        break
    
print(ans)
    
