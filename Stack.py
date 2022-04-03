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