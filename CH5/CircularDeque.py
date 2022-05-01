from CH5.Queue import CircularQueue

MAX_QUEUE_SIZE = 10


class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, elem):
        self.enqueue(elem)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()

    def addFront(self, elem):
        if not self.isFull():
            self.arr[self.front] = elem
            self.front -= 1
            if self.front < 0: self.front = MAX_QUEUE_SIZE - 1

    def deleteRear(self):
        if not self.isEmpty():
            elem = self.arr[self.rear]
            self.rear -= 1
            if self.rear < 0: self.rear = MAX_QUEUE_SIZE - 1
            return elem

    def getRear(self):
        return self.arr[self.rear]