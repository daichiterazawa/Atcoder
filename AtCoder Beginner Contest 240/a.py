# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:57:07 2022

@author: terad
"""

a,b = map(int,input().split())
if b == 10:
    if a == 9 or a == 1:
        print('Yes')
    else:
        print('No')
else:
    print('Yes' if b-a==1 else 'No')

