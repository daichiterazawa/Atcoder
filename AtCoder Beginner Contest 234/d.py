# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:45:07 2022

@author: terad
"""


N,K = map(int,input().split())
P = list(map(int,input().split()))
Q = sorted(P,reverse = True)

index = K-1
ans = []

#配列の後ろから見る
for i in range(N-1,K-2,-1):
    print(Q[index])
    #ポップした値が現在の答えより大きければ
    a = P[i]
    if a >= Q[index]:
        index -= 1
        