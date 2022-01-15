# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:54:23 2022

@author: terad
"""
n = list(input())
num = 0
ans = 0
for i in n:
    num += int(i)
    
ans = num*100 + num *10 + num

print(ans)
