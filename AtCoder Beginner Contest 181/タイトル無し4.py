# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:59:53 2022

@author: terad
"""


X = int(input())
Y = X
Z = []
MOD = 998244353

while Y > 3 :
    if Y % 2 == 0:
        Z.append(0)
        Y = Y // 2
    else:
        Z.append(1)
        Y = Y // 2

Z.reverse()
ans = Y

for z in Z:
    if z == 0:
        ans *= (ans // Y * Y)
        ans = ans % MOD
    else:
        ans *= (ans // Y * (Y+1))
        ans = ans % MOD
        
        
        
print(ans % MOD)