def solution(n):
    # 삼진법 = ternary
    ternary = ""
    while n > 0:
        ternary += str(n % 3)
        n //= 3

    # 십진법 = decimal
    decimal = int(ternary, 3)

    return decimal
