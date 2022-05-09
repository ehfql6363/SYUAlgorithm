def facRep(n):
    temp = n
    while temp > 1:
        n *= temp - 1
        temp -= 1
    return n


print(facRep(3))
