N = int(input())
P = list(map(int, input().split()))

P.sort()

Sum = 0
Prev = 0
for i in range(N):
    Prev += P[i]
    Sum += Prev

print(Sum)
