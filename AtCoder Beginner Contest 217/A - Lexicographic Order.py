# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:50:36 2021

@author: terad
"""

S,T = map(str,input().split())
origin = [S,T]
zisyo = sorted(origin)
 
print('Yes' if origin == zisyo else 'No')