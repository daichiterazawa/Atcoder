# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:33:24 2022

@author: terad
"""
import math
import sys

#データをインプット
N = int(input())
A_list = list(map(int,input().split()))

#最大公約数を求める
g = 0
for i in range(N):
    g = math.gcd(g,A_list[i])

#操作の数をカウント
cnt = 0
for a in A_list:
    a /= g
    
    while a%2==0 :
        a /= 2
        cnt += 1
        
    while a%3==0:
        a /= 3
        cnt += 1
        
    if a != 1:
        print(-1)
        sys.exit()
        
print(cnt)
    