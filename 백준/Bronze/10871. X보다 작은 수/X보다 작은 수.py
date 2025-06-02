n_length, threshold = map(int, input().split())
sequence = list(map(int, input().split()))

for number in sequence:
    if number < threshold:
        print(number, end=' ')