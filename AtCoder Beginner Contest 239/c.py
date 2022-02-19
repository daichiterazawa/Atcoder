# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:36:46 2022

@author: terad
"""
import sys

x1,y1,x2,y2 = map(int,input().split())

list1 = [[x1+1,y1+2],[x1+2,y1+1],[x1+2,y1-1],[x1+1,y1-2],[x1-1,y1-2],[x1-2,y1-1],[x1-2,y1+1],[x1-1,y1+2]]
list2 = [[x2+1,y2+2],[x2+2,y2+1],[x2+2,y2-1],[x2+1,y2-2],[x2-1,y2-2],[x2-2,y2-1],[x2-2,y2+1],[x2-1,y2+2]]

for x,y in list1:
    if [x,y] in list2:
        print('Yes')
        sys.exit()
        
print('No')
        