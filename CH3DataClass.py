class ArrayList():
    def __init__(self, list=[]):
        self.items = list

    def insert(self, pos, elem):
        self.items.insert(pos, elem)

    def delete(self, pos):
        self.items.pop(pos)


list1 = ArrayList([1, 2, 3, 4])
print(list1.items)
list1.insert(2,100)
print(list1.items)
list1.delete(0)
print(list1.items)