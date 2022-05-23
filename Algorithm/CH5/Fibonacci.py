def fibByDnC(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibByDnC(n-1) + fibByDnC(n-2)

def fibIter(n):
    if n<0 : return 0
    last = 0
    cur = 1
    for i in range(2, n+1):
        temp = cur
        cur += last
        last = temp

    return cur