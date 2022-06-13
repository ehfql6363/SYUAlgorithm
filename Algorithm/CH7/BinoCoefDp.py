def binoCoefDp(n, k):
    C = [[-1 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

def binoCoefMem(n, k, C):
    if C[n][k] == None:
        if k == 0 or k == n:
            C[n][k] = 1
        else:
            C[n][k] = binoCoefMem(n-1, k-1, C) + binoCoefMem(n-1, k, C)
    return C[n][k]

def bioMem1(n, k):
    C = [0 for _ in range(k+1)]
    C[0] = 1

    for i in range(1, n+1):
        j = min(i, k)
        while j > 0:
            C[j] = C[j-1] + C[j]
            j -= 1

    return C
print(bioMem1(5, 3))