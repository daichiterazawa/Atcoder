# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:45:45 2022

@author: terad
"""

A,B,C = map(int,input().split())

if A > B :
    print('Takahashi')
elif B > A :
    print('Aoki')
else:
    if C == 0:
        print('Aoki')
    else:
        print('Takahashi')