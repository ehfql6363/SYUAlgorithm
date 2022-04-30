from CH6.LinkedStack import Node


class LinkedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def size(self):
        n = self.head
        count = 0
        while not n == None:
            n = n.link
            count += 1
        return count

    def display(self, msg='LinkedList'):
        node = self.head
        print(msg, end='')
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

    def getNode(self, pos): # pos번 째 노드 가져오기
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos): #pos번 째 노드의 데이터 가져오기
        node = self.getNode(pos)
        if node is None: return None
        else: return node.data

    def replace(self, pos, elem): #pos번 째 노드의 데이터를 elem으로 대체
        node = self.getNode(pos)
        if node is not None:
            node.data = elem

    def find(self, data): #데어터가 data인 노드 반환
        node = self.head
        while not node is None:
            if node.data == data:
                return node
            node = node.link
        return None

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before is None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before is None:
            if self.head != None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link
