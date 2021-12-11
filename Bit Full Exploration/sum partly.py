from  itertools import product

N,W = map(int, input().split())
A = list(map(int,input().split()))
ans = 0

for pro in product((0,1), repeat=N):
    w = 0
    for i,p in enumerate(pro,0):
        w += A[i] * p
    if W == w:
        ans += 1
        
print(ans)
    
 