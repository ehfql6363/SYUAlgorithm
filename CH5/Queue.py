MAX_QUEUE_SIZE = 10


class CircularQueue():
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr = [None] * MAX_QUEUE_SIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % MAX_QUEUE_SIZE

    def clear(self):
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QUEUE_SIZE
            self.arr[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QUEUE_SIZE
            return self.arr[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.arr[(self.front + 1) % MAX_QUEUE_SIZE]

    def size(self):
        return (self.rear - self.front + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.arr[self.front + 1:self.rear + 1]
        else:
            out = self.arr[self.front + 1:MAX_QUEUE_SIZE] + self.arr[0:self.rear + 1]
        print(f"front = {self.front}, rear = {self.rear} => ", out)

