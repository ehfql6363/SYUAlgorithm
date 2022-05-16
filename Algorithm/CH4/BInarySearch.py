def binarySearch(A, key, left, right):
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            right = mid-1
        elif A[mid] > key:
            left = mid+1
    return -1

