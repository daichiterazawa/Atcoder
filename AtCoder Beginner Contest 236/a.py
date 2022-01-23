# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:51:54 2022

@author: terad
"""

S = list(input())
a,b = map(int,input().split())

A,B = a-1,b-1
S[A],S[B] = S[B],S[A]

print(''.join(S))