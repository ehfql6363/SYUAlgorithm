from Algorithm.CH4.KthMin import partition


def quickSort(arr, left, right):
    if left<right:
        mid = partition(arr, left, right)
        quickSort(arr, left, mid)
        quickSort(arr, mid+1, right)

data = [3,1,7,8,2,4,10,5,9]
print("before : ", data)
quickSort(data, 0, len(data)-1)
print("after : ", data)