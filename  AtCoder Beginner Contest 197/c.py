# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 12:12:43 2021

@author: terad
"""
import itertools

N = int(input())
A = list(map(int,input().split()))
ans = 2147483647


for thr in itertools.product((True,False),repeat=N-1):
    num = 0
    orlist = []
    ornum = A[0]
    
    for i,t in enumerate(thr):
        
        #Trueならor計算
        if t:
            ornum |=  A[i+1]
        else:
            orlist.append(ornum)
            ornum = A[i+1]
        
    orlist.append(ornum)
    
    for i in orlist:
        num ^= i
    
    if ans > num:
        ans = num
    


            
print(ans)
    
    
    