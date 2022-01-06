# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 22:35:01 2022

@author: terad
"""

N = int(input())
ans = 0

def eight(num):
    l = []
    while num != 0:
        l.append(str(num % 8))
        num = num // 8
    return l[::-1]
        
    
for n in range(1,N+1):
    n10 = list(str(n))
    n8 = eight(n)
    
    if not('7' in n10) and not('7' in n8):
        ans += 1
        
print(ans)