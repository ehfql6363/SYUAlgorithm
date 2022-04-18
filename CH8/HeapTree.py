class MaxHeap():
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self): return len(self.heap)-1
    def isEmpty(self): return self.size() == 0
    def parent(self, i): return self.heap[i//2]
    def left(self, i): return self.heap[i*2]
    def right(self, i): return self.heap[i*2+1]
    def display(self, msg = '힙 트리 : '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while i != 1 and n > self.parent(i):
            self.heap[i] = self.parent(i)
            i = i//2
        self.heap[i] = n

    def delete(self):
        parentNode = 1
        childNode = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while childNode <= self.size():
                if childNode<self.size() and self.left(parentNode)<self.right(parentNode):
                    childNode += 1
                if last >= self.heap[childNode]:
                    break
                self.heap[parentNode] = self.heap[childNode]
                parentNode = childNode
                childNode *= 2

            self.heap[parentNode] = last
            self.heap.pop(-1)
            return hroot