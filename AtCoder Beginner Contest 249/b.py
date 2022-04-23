# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:56:23 2022

@author: terad
"""

from collections import Counter

S = input()
check = 0

countS = Counter(S)
if countS.most_common()[0][1] > 1:
    check = 1
    

if S.isupper() or S.islower():
    check = 1
    
print('Yes' if check == 0 else 'No')
    
 
        


