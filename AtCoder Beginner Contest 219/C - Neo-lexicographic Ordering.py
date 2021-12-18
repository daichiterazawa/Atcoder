# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:38:07 2021

@author: terad
"""

X = list(input())
N = int(input())
S =[]
S_num = []
 
#高橋アルファベットの辞書を作成
d = {al : i for i,al in enumerate(X)}

#アルファベット番号とアルファベットを2次元配列で格納
for n in range(N):
    S = list(input())
    for m in range(len(S)):
        
