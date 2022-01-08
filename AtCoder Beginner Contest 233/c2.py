# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:18:30 2022

@author: terad
"""

N,X = map(int,input().split())
num = [1]
ans = 0

for n in range(N):
    l,*a = map(int,input().split())
    num = [x * y for x in num for y in a if x*y <= X]
    
ans = num.count(X)

print(ans)
    
    