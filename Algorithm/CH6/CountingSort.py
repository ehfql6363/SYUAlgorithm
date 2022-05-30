MAX_VAL = 10

data = [1, 5, 2, 3, 4, 5, 7, 3, 4, 5, 6, 7, 8, 9, 4, 0]
print("Original DataSet : ", data)


def countingSort(arr):
    out = [0] * len(arr)
    count = [0] * (MAX_VAL)

    for i in arr:
        count[i] += 1  # arr에 들어있는 요소 카운트
    print("count : ", count)

    for i in range(1, MAX_VAL):
        count[i] += count[i - 1]  # 카운트 한 요소의 개수를 누적 합
    print("after : ", count)

    for i in range(len(arr)):
        out[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    for i in range(len(arr)):
        arr[i] = out[i]


countingSort(data)
print("After data : ", data)