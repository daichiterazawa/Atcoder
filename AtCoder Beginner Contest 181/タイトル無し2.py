# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:01:19 2022

@author: terad
"""
from itertools import permutations
i = 0

for P in permutations(range(1,21)):
    print(P)
    i += 1
    if i >= 1000 :
        break
