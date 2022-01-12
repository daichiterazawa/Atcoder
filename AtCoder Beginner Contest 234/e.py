# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:24:05 2022

@author: terad
"""
import sys
import math

X = int(input())

#Xが1桁の場合
if X//10 == 0:
    print(X)
    sys.exit()
    
    
#等差数を小さい順に数え上げ

#桁数
for i in range(2,19):
    #初項
    for j in range(1,10):        
        #公差
        for k in range(math.ceil(-j/(i-1)),math.floor((9-j)/(i-1))+1):
            check = 0
            for l in range(i):
                check += (j+k*(l)) * 10**(i-l-1) 
            
            if check >= X:
                print(check)
                sys.exit()