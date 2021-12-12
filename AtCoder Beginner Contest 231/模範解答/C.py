# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 14:12:28 2021

@author: terad
"""

import bisect

N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

for _ in range(Q):
  x = int(input())
  less_num = bisect.bisect_left(A,x)
  print(N - less_num)