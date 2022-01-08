# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:45:05 2022

@author: terad
"""
import numpy as np

K = int(input())
l = []
ans = 0

while K != 0:
    l.append(K%2)
    K = K//2

lnp = np.array(l)
lans = lnp * 2

for i in range(len(lans)):
    ans += lans[i] * 10**i
    
print(ans)
    
    
    

