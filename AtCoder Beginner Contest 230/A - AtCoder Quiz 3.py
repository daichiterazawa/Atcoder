# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:00:39 2021

@author: terad
"""

N = int(input())
if N <= 9:
    print("AGC00{}".format(N))
    
elif N <= 41:
    print("AGC0{}".format(N))
else :
    print("AGC0{}".format(N+1))