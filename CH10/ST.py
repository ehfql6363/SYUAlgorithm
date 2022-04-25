def topologicalSort(vertex, graph):
    n = len(vertex)
    inDeg = [0] * n

    for i in range(n):
        for j in range(n):
            if