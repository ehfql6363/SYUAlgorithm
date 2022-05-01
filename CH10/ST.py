import collections

def bfsST(graph, start):
    visited = set([start])
    queue = collections.deque([start])
    while queue:
        vtx = queue.popleft()
        nbr = graph[vtx] - visited
        for u in nbr:
            print(f"({v}, {u})", end='')
            visited.add(u)
            queue.append(u)