from CH5.Queue import CircularQueue

MAX_QUEUE_SIZE = 10
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front-1
            if self.front < 0 : self.front = MAX_QUEUE_SIZE - 1

    def deleteRear(self):
        if not self.isFull():
            item = self.rear
            self.rear -= 1
            if self.rear < 0 : MAX_QUEUE_SIZE - 1

    def getRear(self):
        return self.items[self.rear]