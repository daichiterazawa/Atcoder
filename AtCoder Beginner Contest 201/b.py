# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:50:59 2021

@author: terad
"""

N = int(input())
doc = []
for n in range(N):
    s,t = map(str,input().split())
    doc.append([int(t),s])
    
doc.sort()
print(doc[N-2][1])
