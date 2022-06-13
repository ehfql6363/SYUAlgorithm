def lcsDP(str1, str2):
    m = len(str1)
    n = len(str2)
    L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i - 1] == str2[j - 1]: # 마지막 글자가 같은 경우,
                L[i][j] = L[i - 1][j - 1] + 1 #마지막 글자(1) + 마지막을 제외한 나머지 길이
            else: # 마지막 글자가 다르면,
                L[i][j] = max(L[i - 1][j], L[i][j - 1]) # 각 문자열의 마지막을 하나씩만 포함하여 LCS의 길이가 가장 큰 것으로 설정

    return L


def lcsDpTracback(str1, str2, L):
    lcs = ""
    i = len(str1)
    j = len(str2)

    while i > 0 and j > 0:
        v = L[i][j]

        if v > L[i][j - 1] and v > L[i - 1][j] and v > L[i - 1][j - 1]:
            i -= 1
            j -= 1
            lcs = str1[i] + lcs

        elif v == L[i][j - 1] and v > L[i - 1][j]:
            j -= 1
        else:
            i -= 1

    return lcs


str1 = "GAME OVER"
str2 = "HELLO WORD"
L = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
table = lcsDP(str1, str2)
print("str1 = ", str1)
print("str2 = ", str2)
for i in range(len(table)):
    print(table[i])

print(lcsDpTracback(str1, str2, lcsDP(str1, str2)))
