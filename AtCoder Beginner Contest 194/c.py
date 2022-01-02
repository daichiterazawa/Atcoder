# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:28:19 2022

@author: terad
"""

from itertools import combinations

N = int(input())
A = list(map(int,input().split()))
ans = 0

for t in combinations(A,r=2):
    ans += (t[0] - t[1])**2

print(ans)