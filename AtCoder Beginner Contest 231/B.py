# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:19:57 2021

@author: terad
"""
N = int(input())
a = []
b = []

for _ in range(N):
    name = input()
    if name not in a:
        a.append(name)
        b.append(0)
        
    for i,kouho in enumerate(a):
        if kouho == name:
            b[i] += 1
            
print(a[b.index(max(b))])
        
        
        

