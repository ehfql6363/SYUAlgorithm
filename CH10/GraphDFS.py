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

def dfs(graph, start, visited = set()):
    if start not in visited:
        visited.add(start)
        print(start, end=" ")
        nbr = graph[start] - visited #차집합. 즉, 방문한 노드를 제외한 것만 이웃노드로 지정
        nbrList = list(nbr)
        nbrList.sort()
        for v in nbrList:
            dfs(graph, v, visited)

dfs(graph, 'A')