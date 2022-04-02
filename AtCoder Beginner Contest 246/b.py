# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 20:45:47 2022

@author: terad
"""

A,B = map(int,input().split())

print(A/(A**2+B**2)**0.5,B/(A**2+B**2)**0.5)