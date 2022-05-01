graph = {'A': {'B', 'C'},
         'B': {'A', 'D'},
         'C': {'A', 'D', 'E'},
         'D': {'B', 'C', 'F'},
         'E': {'C', 'G', 'H'},
         'F': {'D'},
         'G': {'E', 'H'},
         'H': {'E', 'G'}}


# for i in graph:
#     print(f"노드 {i}와 인접한 노드 = {graph[i]}")

def dfs(graph, start, visited=set()):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)
