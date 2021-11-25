import numpy as np 

N,X = map(int, input().split())
A = np.zeros((2,N+1),dtype = int)
A[0,1:] = np.array(list(map(int, input().split())))



while(1):
    #Xが秘密を知っていたかをチェック
    if A[1,X]==1:
        break
    else :
        #友人Xが秘密を知る
        A[1,X] = 1
    #Xが秘密を教える
    X = A[0,X]
    
print(sum(A[1,:]))
    
    
    
