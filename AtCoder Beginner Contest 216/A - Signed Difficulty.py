# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:52:07 2021

@author: terad
"""

N = float(input())
X,Y = divmod(N,1)
print(int(X),end = '')
if Y < 0.25:
    print('-')
elif Y > 0.65 :
    print('+')
    