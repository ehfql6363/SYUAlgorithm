def fibDpMem(n, mem):
    if mem[n] == None:
        if n < 2:
            mem[n] = n
        else:
            mem[n] = fibDpMem(n-1, mem) + fibDpMem(n-2, mem)

    return mem[n]

def fibDpTab(n):
    f = [None] * (n+1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1]+f[i+2]

    return f[n]
