def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minIdx = i
        for j in range(i+1, n):#가장 작은 값을 갖는 인덱스 찾기
            if arr[minIdx] > arr[j]:
                minIdx = j

        temp = arr[minIdx]
        arr[minIdx] = arr[i]
        arr[i] = temp

        printStep(arr, i+1)

        #arr[i], arr[minIdx] = arr[minIdx], arr[i]

    print(arr)

def printStep(arr, index):
    print(f"Step {index} = ", end="")
    print(arr)


# arr = [3,4,5,2,6,1,8,9,7,0]
# print("원래 배열:",arr)
# selectionSort(arr)