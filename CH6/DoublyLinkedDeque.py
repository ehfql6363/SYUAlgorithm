class DNode():
    def __init__(self, prev, elem, next):
        self.prev = prev
        self.elem = elem
        self.next = next

class DoublyLinkedDeque():
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None
    def clear(self):
        self.front = None
        self.rear = None
    def size(self):
        if self.isEmpty(): return 0
        else:
            node = self.front
            count = 1
            while node != self.rear:
                node = node.next
                count += 1
            return count
    def display(self, msg = 'DoublyLinkedDeque'):
        print(msg, end = ' ')
        if not self.isEmpty():
            node = self.front
            while not node == self.rear:
                print(node.data, end='')
                node = node.next
            print(node.data, end='')
        print()

    def addFront(self, elem):
        node = DNode(None, elem, self.front)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def addRear(self, elem):
        node = DNode(self.rear, elem, None)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.elem
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.elem
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data
