def quickSelection(A, left, right, k):
    pos = partition(A, left, right) #기준 인덱스 설정 (무조건 중간은 아님)

    if pos + 1 == left + k:
        return A[pos]
    elif pos + 1 > left + k:
        return quickSelection(A, left, pos - 1, k)
    else:
        return quickSelection(A, pos + 1, right, k - (pos + 1 - left))


def partition(A, left, right):
    lo = left + 1
    hi = right

    pivot = A[left]

    while lo <= hi:
        while lo <= right and A[lo] <= A[pivot]:
            lo += 1
        while hi > left and A[hi] >= A[pivot]:
            hi -= 1

        if lo < hi:
            A[hi], A[lo] = A[lo], A[hi]

    A[hi], A[pivot] = A[pivot], A[hi]

    return hi


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("배열 : ", arr)
print("[축소정렬] 3번째 작은 수 = ", quickSelection(arr, 0, len(arr) - 1, 3))
