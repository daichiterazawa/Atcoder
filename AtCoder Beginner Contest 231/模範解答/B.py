# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:54:40 2021

@author: terad
"""
from collections import Counter
N = int(input())
C = Counter()

for _ in range(N):
    s = input()
    C[s] += 1
    
m_name,M_num = C.most_common(1)[0]
print(m_name)
