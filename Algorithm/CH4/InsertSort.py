from Algorithm.CH3.SelectionSort import printStep


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i] #정렬할 값 선택(다음)
        j = i - 1 #정렬할 값의 바로 전 인덱스(다음 -1)
        while j >= 0 and A[j] > key: #j가 0보다 크고 j번째 값이 정렬할 값보다 크다면
            A[j + 1] = A[j] #정렬할 값보다 큰 j 번째 값을 원래 인덱스보다 한칸 오른쪽으로 이동
            j = j - 1 #비교할 인덱스를 하나 줄임
        A[j + 1] = key #key가 j인덱스의 값보다 크므로 그 다음 값에 삽입
        printStep(A, i)


data = [5,3,6,2,1,9,0,7,8]
print("원래 배열", data)
insertion_sort(data)