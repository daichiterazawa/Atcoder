# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:24:59 2021

@author: terad
"""

X = float(input())
Y = X - X//1
print(int(X//1) if Y < 0.5 else int(X//1 + 1))
