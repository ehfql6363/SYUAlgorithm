def findStr(str, patern):
    for i in range(len(str) - len(patern) + 1):
        j = 0
        while j < len(patern) and str[j+i] == patern[j]:
            j += 1
        if j == len(patern):
            return i

    return -1

str = "bruteforce"
patern = "fo"

print(findStr(str, patern))