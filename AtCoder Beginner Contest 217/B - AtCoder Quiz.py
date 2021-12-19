# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:21:38 2021

@author: terad
"""

S_set = {'ABC','ARC','AGC','AHC'}

for _ in range(3):
    S = input()
    S_set = S_set - {S}
    
print(S_set.pop())
