# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:05:55 2022

@author: terad
"""
import heapq

N,K = map(int,input().split())
P = list(map(int,input().split()))

hq = P[:K]
heapq.heapify(hq)
print(hq[0])

for x in P[K:]:
    heapq.heappush(hq,x)
    heapq.heappop(hq) #K＋１番目に大きい値を削除
    print(hq[0])
    
    