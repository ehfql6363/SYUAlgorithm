def mergeSort(arr, left, right):
    if left<right:
        mid = (left+right)//2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    k = left
    i = left
    j = mid+1
    while i<=mid and j<=right:
        if arr[i] <= arr[j]:
            sorted[k] = arr[i]
            i, k = i+1, k+1
        else:
            sorted[k] = arr[j]
            j, k = j+1, k+1

    if i > mid: #왼쪽 부분 배열이 먼저 끝나면, 오른 쪽 부분 배열의 남은 부분을 전부 복붙
        sorted[k:] = arr[j:]
        # sorted[k:k+right+1-j] = arr[j:right+1]
    else: #오른쪽 부분 배열이 먼저 끝나면, 왼쪽 부분 배열의 남은 부분을 전부 복붙
        sorted[k:] = arr[i:]
        # sorted[k:k+mid+1-i] = arr[i:mid+1]

    #원래 배열로 복붙
    arr[left:right+1] = sorted[left:right+1]

data = [3,1,7,8,2,4,10,5,9]
sorted = [0] * len(data)
print("before : ", data)
mergeSort(data, 0, len(data)-1)
print("after : ", data)