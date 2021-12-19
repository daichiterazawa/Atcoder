# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:38:07 2021

@author: terad
"""

X = list(input())
N = int(input())
S = []

S_num = []
 
#高橋アルファベット順をabcd順になおす
d = {al_af : chr(i+97)  for i,al_af in enumerate(X)}


#アルファベット番号とアルファベットを2次元配列で格納
for n in range(N):
    S1 = []
    S2 = []
    S1 = list(input())
    #jは文字
    for j in S1:
        S2.append(d[j])
        
    S.append([''.join(S2),''.join(S1)])
    
S.sort()

for i in range(N):
    print(S[i][1])
    
        
        
    
