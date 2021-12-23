N = int(input())
A = list(input())
 
for n in range(N):
  if A[n] == '1':
    if n%2==0:
      print('Takahashi')
    else:
      print('Aoki')
    break