# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:01:59 2021

@author: terad
"""
N,X = map(int,input().split())
A = list(map(int,input().split()))
print('Yes' if X>=sum(A)-N//2 else 'No')
