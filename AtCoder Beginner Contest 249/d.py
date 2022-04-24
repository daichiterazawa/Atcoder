# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:56:21 2022

@author: terad
"""
from collections import Counter


#Ajについて全探索
def main():
    ans = 0
    N = int(input())
    A = map(int,input().split())
    AC = Counter(A)
    
    for aj in range(1,2*10**5+1):
        for ai in range(aj,2*10**5+1,aj):
            ak = ai // aj
            ans += AC[ak] * AC[aj] * AC[ai]
    
    print(ans)
    
if __name__ == '__main__':
    main()
            
    
    