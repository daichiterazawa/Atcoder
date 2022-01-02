# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 13:33:54 2022

@author: terad
"""
from collections import Counter

N = int(input())
A = list(map(int,input().split()))
ans = 0

#値の種類と出現数を数える
cnt = Counter(A)

for i in range(-199,201):
    for j in range(-200,i):
        ans += (i-j)**2 * cnt[i] * cnt[j]

print(ans)
    
