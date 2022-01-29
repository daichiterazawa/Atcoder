# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:24:00 2022

@author: terad
"""

S = list(input())
K = int(input())
l = 0
ans = 0

for i,s in enumerate(S):
    #置き換えに余裕がある場合
    if K != 0:
        if s == '.':  
            S[i] = 'O'
            K -= 1     
    
    #置き換えに余裕がない場合    
    else :
        if s == '.':
            #左側をポップ
            for j in range(0,len(S)):
                if S[l+j] == 'O' or i == l+j:
                    l += j+1
                    break
            S[i] = 'O'
            
                
        
                
    ans = max(ans,i-l+1)
                   
    
               
print(ans)
                
            
            
            
        
        
    