# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:59:52 2022

@author: terad
"""
from collections import deque

X = int(input())
ans = 1
MOD = 998244353
d = deque([X])

while d :
    x = d.popleft()
    if x > 4:
        if x % 2 == 0:
            d.append(x//2)
            d.append(x//2)
        else:
            d.append(x//2)
            d.append(x//2 + 1)
    else:
        ans *= x % MOD
        
print(ans % MOD)
