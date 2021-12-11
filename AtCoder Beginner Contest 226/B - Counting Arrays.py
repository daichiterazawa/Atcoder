######### 初見正解不可だったため、模範解答を見たうえで回答

N = int(input())
S = set()

for _ in range(N):
    L,*a = map(int,input().split())
    S.add(tuple(a))
    

print(len(S))


    