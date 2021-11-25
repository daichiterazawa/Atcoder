# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 17:07:04 2021

@author: terad
"""
import numpy as np

N,K = map(int,input().split())
P = np.zeros((N,3),dtype=int)
for i in range(N):
    P[i,:] = np.array(list(map(int,input().split())))
    
#K位に入るために必要な点数を求める
sum_P = np.sum(P, axis=1)
sort_P = np.sort(sum_P)[::-1]
border = sort_P[K-1] - 300

for i in range(N):
    print('Yes' if sum_P[i]>=border else 'No')



