# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 23:17:03 2022

@author: terad
"""  
###############################
#ほぼ写経、要復習
###########################
Q = int(input())
T = [0] * Q
X = [0] * Q
N = 2**20

for q in range(Q):
    T[q],X[q] = map(int,input().split())
    
#リスト作成
A = [-1] * 2**20

#各Aの根を保存するリスト
P = list(range(N))

for t,x in zip(T,X):
    if t == 1:
        h = x % N
        pos = h
        visited = [pos]
        
        while A[pos] != -1:
            pos = P[pos]
            visited.append(pos)
        
        A[pos] = x
        new_P = P[(pos+1) % N]
        for v in visited:
           P[v] =  new_P
            
        
    else:
        print(A[x%N])
