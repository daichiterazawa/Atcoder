# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 23:04:46 2022

@author: terad
"""
from typing import List

class UnionFind:
    
    def __init__(self,n):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n
        
    def unite(self,x,y) -> bool:
        """xとyをマージ"""
        x = self.root(x)
        y = self.root(y)
        
        if x == y:
            return False
        
        self.__group_count -= 1
        
        if self.parent[x] > self.parent[y]:
            x,y = y,x
            
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        
        return True
    
    def is_same(self,x,y) -> bool:
        return self.root(x) == self.root(y)
    
    def root(self,x) -> int:
        '''xの根を取得'''
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
        
    def size(self,x) -> int:
        return -self.parent[self.root(x)]
    
    def all_sizes(self) -> List[int]:
        """全連結成分のサイズのリストを取得O(n)"""
        
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
                
        return sizes
    
    def groups(self) -> List[List[int]]:
        """全連結成分の内容のリストを取得"""
        groups = dict()
        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)
        return list(groups.values())
    
    @property
    def group_count(self) -> int:
        return self.___group_count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        