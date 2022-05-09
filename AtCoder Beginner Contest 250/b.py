# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:31:34 2022

@author: terad
"""

N,A,B = map(int,input().split())

for i in range(N * A):
    for j in range(N * B):
        if (j // B) % 2 == 0:
            if (i // A) % 2 == 0:
                print('.',end='')
            else:
                print('#',end='')
        else:
            if (i // A) % 2 == 0:
                print('#',end='')
            else:
                print('.',end='')
            
    print('\n',end='')
    
