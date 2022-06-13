def editDist(str1, str2, n, m, mem):
    if n == 0: return n
    if m == 0: return m

    if mem[n - 1][m - 1] == None:
        if str1[n - 1] == str2[m - 1]:
            mem[n - 1][m - 1] = editDist(str1, str2, n - 1, m - 1, mem)

        else:
            mem[n - 1][m - 1] = 1 + \
                                min(editDist(str1, str2, n - 1, m, mem),
                                    editDist(str1, str2, n, m - 1, mem),
                                    editDist(str1, str2, n - 1, m - 1, mem))

        print(f"mem[{n-1}][{m-1}] = {mem[n-1][m-1]}")

    return mem[n - 1][m - 1]


str1 = "tuesday"
str2 = "thursday"
n = len(str1)
m = len(str2)
mem = [[None for _ in range(m)] for _ in range(n)]
print("편집거리 :", editDist(str1, str2, n, m, mem))

print()
for i in range(len(mem)):
    for j in range(len(mem[i])):
        if mem[i][j] == None:
            print(" NONE ", end='')
        else:
            print(f"{mem[i][j]: ^6d}", end='')
    print()