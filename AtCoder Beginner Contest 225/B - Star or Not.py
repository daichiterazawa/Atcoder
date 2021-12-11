# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:04:54 2021

@author: terad
"""

N = int(input())
a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
node = 0
for ab1 in [a1,b1]:
    for ab2 in [a2,b2]:
        if ab1 == ab2:
            node = ab1
            
for _ in range(N-3):
    a,b = map(int,input().split())
    if node == a or node == b:
        node = node
    else:
        node = 0
        
print('Yes' if node != 0 else 'No')
