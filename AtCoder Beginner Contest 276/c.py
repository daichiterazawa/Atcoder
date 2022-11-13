# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:52:48 2022

@author: terad
"""

N = int(input())
P = list(map(int,input().split()))


#下位2桁から見ていく
#順に小さくなったら繰り返す
for i in range(N-1,0,-1):
    ue,sita = P[i-1],P[i]
    if ue > sita:
      target = ue
      target_list = sorted(P[i-1::],reverse=True)
      idx = target_list.index(ue)
      break
      
for ans in P[:i-1]:
    print(ans,end=' ')
    
print(target_list[i+1],end=' ')

for ans in target_list:
    if ans != target_list[i+1]:
        print(ans,end=' ')