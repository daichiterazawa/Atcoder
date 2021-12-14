# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:21:31 2021

@author: terad
"""
import bisect
N = int(input())
A = []
B = []
C = [0]

for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(C[i] + a/b)


finish_time = C[-1]/2

index = bisect.bisect_right(C,finish_time)
amari_time = finish_time - C[index-1]
print(sum(A[:index-1]) +B[index-1]*amari_time)

    