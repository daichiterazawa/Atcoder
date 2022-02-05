# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 20:55:22 2022

@author: terad
"""

N = int(input())
x = N
y = 1
ans = 0
mod = 998244353

while x//10 != 0:
    ans += int((1 + 9*y) * 9*y // 2) % mod
    y *= 10
    x //= 10
    
ans += int((1 + (N-y+1))*(N-y+1)//2) % mod
ans = ans%mod

print(ans)
    
    



