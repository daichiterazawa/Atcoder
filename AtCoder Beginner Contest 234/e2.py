# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:41:50 2022

@author: terad
"""

from collections import deque

def solve():
    que = deque(range(1,100))
    
    while que:
        num = que.popleft()
        if num >= X:
            return num
        if num >= 10:
            nf = num % 10
            ns = (num//10) % 10
            d = nf - ns
            t = nf + d
            if 0 <= t <= 9:
                que.append(num * 10 + t)
                
X = int(input())
print(solve())