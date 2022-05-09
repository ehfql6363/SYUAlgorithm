def binaryDigits(n):
    count = 0
    while n >= 1:
        count += 1
        n //= 2

    return count

def binaryDigitsRecur(n):
    if n<=1:
        return 1
    else:
        return 1 + binaryDigitsRecur(n//2)

print(binaryDigits(13))
