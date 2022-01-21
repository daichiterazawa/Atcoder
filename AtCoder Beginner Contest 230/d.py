# -*- coding: utf-8 -*-
"""
コツ
順序関係ないときは一度ソートを考える
"""
"""
Created on Fri Jan 21 22:10:18 2022

@author: terad
"""

N,D = map(int,input().split())
LR = [list(map(int,input().split())) for i in range(N)]

LR.sort(key=lambda x: x[1])



x = 0
ans = 0

for l,r in LR:
    if x < l:
        ans += 1
        x = r + D - 1 #パンチの余波が届くギリギリの範囲

print(ans)
        
        
    