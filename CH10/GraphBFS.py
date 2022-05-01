import collections

graph = {'A': {'B', 'C'},
         'B': {'A', 'D'},
         'C': {'A', 'D', 'E'},
         'D': {'B', 'C', 'F'},
         'E': {'C', 'G', 'H'},
         'F': {'D'},
         'G': {'E', 'H'},
         'H': {'E', 'G'}}


def bfs(graph, start):
    visited = set([start])
    queue = collections.deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        nbr = graph[v] - visited
        for next in nbr:
            visited.add(next)
            queue.append(next)
