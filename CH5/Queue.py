MAX_QUEUE_SIZE = 10
class Queue():
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QUEUE_SIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front % MAX_QUEUE_SIZE == (self.rear+1) % MAX_QUEUE_SIZE

    def enqueue(self, elem):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QUEUE_SIZE
            self.items[self.rear] = elem

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QUEUE_SIZE
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % MAX_QUEUE_SIZE]

    def size(self):
        if not self.isEmpty():
            return (self.rear - self.front + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+MAX_QUEUE_SIZE] \
            + self.items[0:self.rear+1]
        print("[f=%s, r=%s ==>"%(self.front, self.rear), out)
