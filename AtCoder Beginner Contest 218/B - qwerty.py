# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:30:54 2021

@author: terad
"""

P = list(map(int,input().split()))

for i in P:
    print(chr(i+96),end="")