# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:09:56 2021

@author: terad
"""

N = int(input())
x = int(1.08 * N)
if x<206:
    print('Yay!')
elif x==206:
    print('so-so')
else:
    print(':(')