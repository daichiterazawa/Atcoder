# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 22:44:05 2022

@author: terad
"""

N = int(input())
A = list(map(int,input().split()))
pre = 0
num_max = 0
for a in A:
    if pre > a:
        num_max = pre
        break
    else:
        pre = a

if num_max == 0:
    num_max = A[-1]
    

for a in A:
    if a != num_max:
        print(a,' ',end='')