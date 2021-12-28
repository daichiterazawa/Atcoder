# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:04:17 2021

@author: terad
"""

N,K = map(int,input().split())
money = K
ans = 0
X = []
for n in range(N):
    a,b = map(int,input().split())
    X.append([a,b])

X.sort()  
    
for n in range(N):    
    if money < X[n][0] :
        break
    else:
        money += X[n][1]

print(money)    