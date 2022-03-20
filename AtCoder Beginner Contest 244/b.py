# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:44:13 2022

@author: terad
"""

N = int(input())
T = list(input())
check = 0
x,y = 0,0

for t in T:
    if t == 'S':
        if check == 0:
            x += 1
        elif check == 1:
            y -= 1
        elif check == 2:
            x -= 1
        else:
            y += 1
            
    else:
        check = (check + 1) % 4
        
print(x,y)
        
            