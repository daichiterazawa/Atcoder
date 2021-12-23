# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:40:02 2021

@author: terad
"""

from bisect import bisect_left 

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
min_num = 10**10

for i in range(M):
    index = bisect_left(A,B[i])
    if index != N:
        num = min(abs(A[index-1]-B[i]),abs(A[index]-B[i]))
    else :
        num = abs(A[index-1]-B[i])
        
    if num<=min_num:
        min_num = num
        
print(min_num)
        