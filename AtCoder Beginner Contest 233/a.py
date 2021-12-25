# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 20:48:46 2021

@author: terad
"""

X,Y = map(int,input().split())
if Y-X <= 0:
    print(0)
elif (Y-X)%10 == 0:
    print((Y-X)//10)
else:
    print((Y-X)//10+1)
    