# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:42:45 2022

@author: terad
"""
import itertools 

N = list(input())
ans = 0


for t in itertools.permutations(N):
    t = list(t)
    for i in range(1,len(N)):
        a,b = int(''.join(sorted(t[:i],reverse=True))),int(''.join(sorted(t[i:],reverse=True)))
        
        if ans <= a*b:
            ans = a*b
            
print(ans)
    
        
    


