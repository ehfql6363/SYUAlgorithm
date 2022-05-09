def uniqueElements(A):
    n = len(A)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i] == A[j]:
                print("False")
                return False

    print("True")
    return True


arr1 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 23, 123]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 123]
uniqueElements(arr1)
uniqueElements(arr2)
