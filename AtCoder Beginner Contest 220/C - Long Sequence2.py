# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:29:25 2021

@author: terad
"""

import numpy as np

N = int(input())
A = list(map(int,input().split()))
A_ruiseki_numpy = np.cumsum(A)
X = int(input())

A_sum = sum(A)
A_len = len(A)

syou,amari = divmod(X,A_sum)

#2分探索で余りが入るインデックスを求める
sabun = np.searchsorted(A_ruiseki_numpy,amari, side='right') + 1

print(A_len * syou + sabun)




