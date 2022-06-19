from queue import Queue
import random

BUCKETS = 10
DIGITS = 4
data = []

for i in range(15):
    data.append(random.randint(1, 9999))
print(data)


def radixSort(arr):
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    factor = 1
    for i in range(DIGITS):
        for j in arr:
            queues[(j // factor) % 10].put(j)

        idx = 0
        for k in range(BUCKETS):
            while not queues[k].empty():
                arr[idx] = queues[k].get()
                idx += 1

        factor *= 10

        print("step", i + 1, arr)


radixSort(data)