# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:24:00 2022

@author: terad
"""

S = input()
K = int(input())
l = 0
check = 0
ans = 0

for i,s in enumerate(S):
    #置き換えに余裕がある場合
    if K != 0:
        if s == '.':  
            S[i] = 'O'
            K -= 1
            check += 1
        else:
            check += 1
    
    #置き換えに余裕がない場合    
    else :
        if s == '.':
            #左側をポップ
            if S[l] == 'X':
                
                if ans < check :
                    ans = check
                
                check -= 1 
                
            else:
                l += 1
                S[i] = 'O'
                
                
            
            
            
        
        
    