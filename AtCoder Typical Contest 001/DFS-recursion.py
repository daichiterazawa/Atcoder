#再帰を用いたDFS

import sys 

sys.setrecursionlimit(10**7)
h,w = map(int,input().split())
c = [list(input()) for i in range(h)]

def dfs(x,y):
    #引き返す場合の条件設定
    if not(0 <= x <= w-1) or not(0 <= y <= h-1) or c[y][x]=='#':
        return
    
    #ゴールを見つけた場合
    if c[y][x] == 'g':
        print('Yes')
        sys.exit()
    
    #探索を続行する場合
    c[y][x] = '#'
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    

#スタート位置を探索
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            sx,sy = j,i
            
dfs(sx,sy)
print('No')
            