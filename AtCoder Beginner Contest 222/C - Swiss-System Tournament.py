# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:24:13 2021

@author: terad
"""

N,M = map(int,input().split())
A = []
win_num = []

for _ in range(2*N):
    win_num.append(0)

#入力受け取り
for n in range(2*N):
    A.append(list(input()))
    
#勝負開始
for m in range(M):
    #対戦相手決定
    
    
    