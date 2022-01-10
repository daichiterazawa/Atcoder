# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 11:04:58 2022

@author: terad
"""


def solve():
    ans = 0
    for i in range(N):
        x1,y1 = XY[i]
        for j in range(N):
            x2,y2 = XY[j]
            d = ((x2-x1)**2 + (y2-y1)**2)**0.5
            ans = max(d,ans)
    return ans

N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]

print(solve())