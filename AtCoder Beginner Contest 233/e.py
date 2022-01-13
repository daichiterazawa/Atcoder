from itertools import accumulate


X = input()
Y = [int(x) for x in X]
Z = list(accumulate(Y))[::-1]
 
l = len(Y)
ans = 0
 
if l >= 10**10 + 2:
    for i,z in enumerate(Z[:l-10**100+1]):
        ans += z * 10**i
    
else:
    for i,z in enumerate(Z):
        ans += z * 10**i


print(ans)
