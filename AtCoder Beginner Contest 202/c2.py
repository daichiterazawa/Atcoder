# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:37:23 2021

@author: terad
"""
def main():
    from collections import Counter
    N = int(input())
    A = list(map(int,input().split()))
    B = [0] + list(map(int,input().split()))
    C = [0] + list(map(int,input().split()))
    
    Acnt = Counter(A)
    ans = 0
    
    for c in C[1:]:
        ans += Acnt[B[c]]
        
    print(ans)
    
if __name__ == '__main__':
    main()