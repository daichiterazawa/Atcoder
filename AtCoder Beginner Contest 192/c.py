# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:43:49 2022

@author: terad
"""



def func(num):
    l = list(str(num))
    g1 = ''.join(sorted(l))
    g2 = ''.join(sorted(l, reverse=True))
    return int(g2) - int(g1)

if __name__ == '__main__':
    N,K = map(int,input().split())
    for _ in range(K):
        N = func(N)

print(N)
        
    
    
    