# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 16:15:03 2021

@author: terad
"""
import bisect

N = int(input())
A = list(map(int,input().split()))
B = [0] + list(map(int,input().split()))
C = [0] + list(map(int,input().split()))
ans = 0
A.sort()

for c in C[1:]:
    l = bisect.bisect_left(A,B[c])
    r = bisect.bisect_right(A,B[c])
    if l != r:
        ans += r-l
          
print(ans)
    