# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:48:33 2021

@author: terad
"""
import itertools

N = int(input())
P_2D = []
check = 0
for _ in range(N):
    P = list(map(int,input().split()))
    P_2D.append(P)

index = itertools.combinations(range(N),3)


for x in index:
    
    if (P_2D[x[0]][1]-P_2D[x[1]][1])*(P_2D[x[2]][0]-P_2D[x[1]][0]) != (P_2D[x[2]][1]-P_2D[x[1]][1])*(P_2D[x[0]][0]-P_2D[x[1]][0]):
        check += 1
print(check)        



    
    