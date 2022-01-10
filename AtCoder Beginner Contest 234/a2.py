# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 10:57:40 2022

@author: terad
"""
def f(t):
    return t**2 + 2*t +3

t = int(input())

print(f(f(f(t)+t)+f(f(t))))


