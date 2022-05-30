NO_OF_CHARS = 128

def shiftTable(pat):
    m = len(pat)
    tb = [m] * NO_OF_CHARS

    for i in range(m - 1):
        tb[ord(pat[i])] = m - 1 - i
    return tb


def horspoolSearch(text, pat):
    m = len(pat)
    n = len(text)
    t = shiftTable(pat)

    i = m - 1

    while i <= n - 1:
        k = 0
        while k <= m - 1 and pat[m - 1 - k] == text[i - k]:
            k += 1
            print("Number of Match, k : ", k)
        if k == m:
            return i - m + 1
        else:
            print(f"i : {i}, text[i]: {text[i]}, t[ord(text[i])]: {t[ord(text[i])]}", end=" ")
            i += t[ord(text[i - k])] - k
            print(f"after skip i: {i}")

    return -1


print("패턴의 위치", horspoolSearch("APPLEMANGOBANANAGRAPE", "BANANA"))
