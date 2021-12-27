# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 18:28:26 2021

@author: terad
"""

n,k = map(int,input().split())
print(int(n*(n+1)/2*100*k + k*(k+1)/2*n))