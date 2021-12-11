# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 22:53:13 2021

@author: terad
"""

A,B = input().split()
X, Y = A.zfill(20), B.zfill(20)

judge = 'Easy'
for x,y  in zip(X,Y):
    if int(x)+int(y) >=10:
        judge = 'Hard'
        
print(judge)
        

    

