# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 21:21:17 2021

@author: terad
"""

S,T,X = map(int, input().split())

if T > S:#日付をまたがないとき
    if X>=S and X<T:
        print('Yes')
    else :
        print('No')
        
else :#日付をまたぐとき
    if X>=S:
        print('Yes')
    elif X<T:
        print('Yes')
    else:
        print('No')
        
        
        
    