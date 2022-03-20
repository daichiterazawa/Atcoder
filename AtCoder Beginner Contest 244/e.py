  
N,M,K,S,T,X = map(int,input().split())
check = [[0]*N for i in range(N)]

for i in range(M):
    u,v = map(int,input().split())
    check[u-1][v-1] = 1
    check[v-1][u-1] = 1
    
A = [[0]*N for i in range(K+1)]
B = [[0]*N for i in range(K+1)]

A[0][S-1] = 1

for i in range(1,K+1):
    for j,a in enumerate(A):
        for
        
    


    
    
   








































