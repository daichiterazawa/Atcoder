# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 10:29:25 2021

@author: terad
"""

N = int(input())
A = list(map(int,input().split()))
#200のあまり
B = [0] * 200

for a in A:
    B[a%200] += 1
    
ans = 0
for b in B:
    if b >= 2:
        ans += b*(b-1)/2

print(ans)
        
