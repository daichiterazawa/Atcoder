# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:21:33 2021

@author: terad
"""

A,B,C = map(int,input().split())
if C%2 == 1:
    if A > B:
        print('>')
    elif A == B :
        print('=')
    else:
        print('<')
else:
    if abs(A) > abs(B):
        print('>')
    elif abs(A) == abs(B) :
        print('=')
    else:
        print('<')