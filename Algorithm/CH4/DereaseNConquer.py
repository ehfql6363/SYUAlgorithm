def factorial_recur(n):
    if n==1:
        return 1
    else :
        return (n*factorial_recur(n-1))

def factorial_iter(n):
    ans = 1
    for i in reversed(range(n)):
        ans *= i

    return ans