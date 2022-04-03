class Stack():
    def __init__(self):
        """

        :rtype: object
        """
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def push(self, elem):
        self.top.append(elem)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

    def size(self):
        return len(self.top)

    def clear(self):
        self.top = []


odd = Stack()
even = Stack()

for i in range(1, 31):
    if i % 2 == 0:
        even.push(i)
    else:
        odd.push(i)

print("oddStack : ", odd.top)
print("evenStack: ", even.top)

for i in range(10):
    odd.pop()
for i in range(5):
    even.pop()

print("oddStack : ", odd.top)
print("evenStack: ", even.top)

odd.clear()
even.clear()

print("oddStack : ", odd.top)
print("evenStack: ", even.top)