import random

M = 13
table = [None] * M


def hashFn(key):
    return key % M


def lpInsert(key):
    id = hashFn(key)
    count = M
    while count > 0 and (table[id] != None and table[id] != -1):
        id = (id + 1) % M
        count -= 1

    if count > 0:
        table[id] = key

    return


print("Original", table)
for _ in range(10):
    randomNumber = random.randint(1, 10)
    lpInsert(randomNumber)
    print(f"{randomNumber} insert: {table}")


def lpSearch(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return None
        if table[id] == key:
            return table[key]
        id = (id + 1) % M
        count -= 1

    return None


print(f"5 탐색 : {lpSearch(5)}")


def lpDelete(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return
        if table[id] == key and table[id] != -1:
            table[id] = -1
            return
        id = (id + 1) % M
        count -= 1


lpDelete(5)
print(f"5삭제 : {table}")