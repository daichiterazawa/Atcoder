# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:24:00 2022

@author: terad
"""

S = input()
K = int(input())
l = 0
ans = 0

for i,s in enumerate(S):
    #置き換えに余裕がある場合
    if K != 0:
        if s == '.':  
            S[i] = 'O'
            K -= 1
            ans += 1
        else:
            ans += 1
    
    #置き換えに余裕がない場合    
    else :
        if s == '.':
            #左側をポップ
            if S[l] == 'X':
                l
                
            
            
            
        
        
    