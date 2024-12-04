N, K = map(int, input().split())  
A = [int(input()) for _ in range(N)]

count = 0  
for coin in reversed(A):  
    count += K // coin  
    K %= coin  
    if K == 0:  
        break

print(count)




