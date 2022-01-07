# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 11:28:15 2021

@author: terad
"""
import numpy as np

R,X,Y = map(int,input().split())
p,q = divmod(np.sqrt(X**2 + Y**2),R)

if q == 0 and p == 1:
    print(1)
elif p <= 1:
    print(2)
else:
    print(int(p+1) if q!=0 else int(p))