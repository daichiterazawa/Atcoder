# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:37:19 2021

@author: terad
"""
P = int(input())
a = 10*9*8*7*6*5*4*3*2*1
ans = 0
for i in range(10):
    b,P = divmod(P,a)
    ans += b
    a /= (10-i)

print(int(ans))    

    