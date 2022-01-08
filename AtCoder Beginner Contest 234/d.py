# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:45:07 2022

@author: terad
"""
import bisect 
import heapq

N,K = map(int,input().split())
P = list(map(int,input().split()))

#Kが2以上として考える
Q = P[:K]
heapq.heapify(Q)
knum = heapq.heappop(Q)
print(min_num)


for i in range(K,N):
    p = P[i]
    if min_num <= p:
        
        
        
    print(Psort[0])
    

        