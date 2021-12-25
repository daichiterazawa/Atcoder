# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 20:48:46 2021

@author: terad
"""

L,R = map(int,input().split())
S = list(input())

s1 = S[:L-1]
s2 = reversed(S[L-1:R])
s3 = S[R:]

for i in s1:
    print(i , end='')
for i in s2:
    print(i , end='')
for i in s3:
    print(i , end='')