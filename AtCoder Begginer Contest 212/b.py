# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:59:56 2021

@author: terad
"""

X_str= list(input())
X = [int(x) for x in X_str] 

if X[0]==X[1] and X[1]==X[2] and X[2]==X[3]:
    print('Weak')
elif (X[0]+1)%10 == X[1] and (X[1]+1)%10 == X[2] and (X[2]+1)%10 == X[3]:
    print('Weak')
else:
    print('Strong')
