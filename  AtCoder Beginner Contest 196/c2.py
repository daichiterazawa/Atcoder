# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 11:09:46 2022

@author: terad
"""

N = int(input())

for i in range(1,1000001):
    num = int(str(i)*2)
    if num > N:
        print(i-1)
        break