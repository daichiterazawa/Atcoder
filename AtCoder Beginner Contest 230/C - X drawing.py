# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:46:49 2021

@author: terad
"""
import numpy as np

N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())

#kがリストの数字なら黒く塗られる
k1 = np.zeros((Q-P+1,S-R+1))
k2 = np.zeros((Q-P+1,S-R+1))




