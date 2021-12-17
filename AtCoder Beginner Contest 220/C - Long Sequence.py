# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:02:28 2021

@author: terad
"""

N = int(input())
A = list(map(int,input().split()))
X = int(input())
A_len = len(A)
A_sum = sum(A)

syou = X // A_sum
amari = X % A_sum

sum=0
check = 0

while sum <= amari:
    sum += A[check]
    check += 1


print(syou*A_len + check)

