# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 20:57:41 2022

@author: terad
"""
import sys

N = int(input())
l = 2

S = []
for i in range(N):
    s = list(input())
    S.append(s)
    
for x in range(N):
    for y in range(N):
    
        for migi in range(6):
            if l != 0:
                if x + migi > N-1:
                    l = 2
                    break
                
                elif S[x+migi][y] == '.':
                    l -= 1
                    
                    if migi == 5:        
                        print('Yes')
                        sys.exit()
                        
                else:
                    if migi == 5:        
                        print('Yes')
                        sys.exit()
                        
            else:
                if x + migi > N-1:
                    l = 2
                    
                    break
                
                elif S[x+migi][y] == '.':
                    l = 2
                    break
                else:
                    if migi == 5:        
                        print('Yes')
                        sys.exit()
        
            
        for sita in range(6):
            if l != 0:
                if y + sita > N-1:
                    l = 2
                    break
                
                elif S[x][y+sita] == '.':
                    l -= 1
                    if sita == 5:        
                        print('Yes')
                        sys.exit()
                        
                else:
                    if sita == 5:        
                        print('Yes')
                        sys.exit()
                    
            else:
                if y + sita > N-1:
                    l = 2
                    break
                
                elif S[x][y+sita] == '.':
                    l = 2
                    break
                
                else:
                    if sita == 5:        
                        print('Yes')
                        sys.exit()
                
        
            
        for naname in range(6):
            if l != 0:
                if y + naname > N-1 or x + naname > N - 1:
                    l = 2
                    break
                
                elif S[x+naname][y+naname] == '.':
                    l -= 1
                    if naname == 5:        
                        print('Yes')
                        sys.exit()
                        
                else:
                    if naname == 5:        
                        print('Yes')
                        sys.exit()
                    
            else:
                if y + naname > N-1 or x + naname > N - 1:
                    l = 2
                    break
                
                elif S[x+naname][y+naname] == '.':
                    l = 2
                    break
                else:
                    if naname == 5:        
                        print('Yes')
                        sys.exit()
                        
        for naname in range(6):
            if l != 0:
                if y + naname > N-1 or x - naname < 0:
                    l = 2
                    break
                
                elif S[x-naname][y+naname] == '.':
                    l -= 1
                    if naname == 5:        
                        print('Yes')
                        sys.exit()
                        
                else:
                    if naname == 5:        
                        print('Yes')
                        sys.exit()
                    
            else:
                if y + naname > N-1 or x - naname < 0:
                    l = 2
                    break
                
                elif S[x-naname][y+naname] == '.':
                    l = 2
                    break
                else:
                    if naname == 5:        
                        print('Yes')
                        sys.exit()
                
print('No')
            
            
            
            
                    
            
        