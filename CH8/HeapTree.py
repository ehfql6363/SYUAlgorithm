class MaxHeap():
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self):
        return len(self.heap) - 1
    def isEmpty(self):
        return self.size() == 0
    def parent(self, i):
        return self.heap[i//2]
    def left(self, i):
        return self.heap[i*2]
    def right(self, i):
        return self.heap[i*2+1]
    def display(self, msg='힙 트리: '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        idx = self.size()
        while idx != 1 and n > self.parent(idx):
            self.heap[idx] = self.parent(idx)
            idx = idx//2
        self.heap[idx] = n

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1] #delete할 때 나오는 값
            last = self.heap[self.size()]
            while child <= self.size():
                if child < self.size() and self.left(parent) < self.right(parent):
                    child += 1
                if last >= self.heap[child]:
                    break

                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot



