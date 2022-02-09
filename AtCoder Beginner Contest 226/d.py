# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:21:06 2022

@author: terad
"""
import math

N = int(input())
XY = []
S = set()

for i in range(N):
    x,y = map(int,input().split())
    XY.append([x,y])
    
for i in range(N):
    for j in range(N):
        if i != j:
            xi,yi = XY[i]
            xj,yj = XY[j]
            #最大公約数を求める
            sdk = math.gcd(xj-xi,yj-yi)
            s = tuple([(xj-xi)//sdk,(yj-yi)//sdk])
            S.add(s)
            
print(len(S))
        
