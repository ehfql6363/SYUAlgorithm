def kanpsackDp(W, wList, vList, n):
    tab = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wList[i-1] > w: # 넣을 물건의 무게가 현재 배낭의 용량보다 크다면,
                tab[i][w] = tab[i-1][w] # 넣을 수 없으으로 전 물건을 넣었을 가치가 옴.
            else:
                valWith = vList[i-1] + tab[i-1][w-wList[i-1]]
                valWithout = tab[i-1][w]
                tab[i][w] = max(valWith, valWithout)

    for i in range(len(tab[0])):
        print(i, end=" | ")

    print()

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end=" | ")
        print()

    return tab[n][w]

wList = [2,5,8,4,7,6]
vList = [60, 100, 190, 120, 200, 150]
W = 18
n = len(wList)

print(kanpsackDp(W, wList, vList,n))
