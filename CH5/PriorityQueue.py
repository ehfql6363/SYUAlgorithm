class PriorityQueue():
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return len(self.arr) == 0
    def size(self):
        return len(self.arr)
    def clear(self):
        self.arr = []

    def enqueue(self, elem):
        self.arr.append(elem)

    def findMaxIndex(self): #배열 안의 값이 제일 큰 인덱스 찾기
        if self.isEmpty(): return None #비어있으면 None 리턴
        else:
            highest = 0 #초기 인덱스
            for i in range(1, self.size()):
                if self.arr[highest] < self.arr[i]: # highest인덱스의 배열 값과 비교하여
                    highest = i # highest 인덱스를 배열의 값이 큰 인덱스로 갱신
            return highest #highest 리턴

    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.arr.pop(highest)

    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.arr[highest]