# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 17:50:57 2021

@author: terad
"""

S,T,X = map(int, input().split())

if S < T:
    print("Yes" if S <= X < T else "No")
else:
    print("Yes" if X < T or S<= X else "No")
    
    
