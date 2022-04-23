# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:55:58 2022

@author: terad
"""

a,b,c,d,e,f,x = map(int,input().split())
taka,ao = 0,0

taka += a*b * (x//(a+c))
if x%(a+c) <= a:
    taka += b * (x%(a+c))
else:
    taka += b * a
    
    
ao += d*e * (x//(d+f))
if x%(d+f) <= d:
    ao += e*(x%(d+f))
else:
    ao += e*d
    
if taka > ao:
    print("Takahashi")
elif taka < ao:
    print("Aoki")
else:
    print("Draw")