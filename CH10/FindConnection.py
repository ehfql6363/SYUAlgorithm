def dfsColor(graph, color, vertex, visited):
    if vertex not in visited:
        visited.add(vertex)
        color.append(vertex)
        nbr = graph[vertex] - visited
        for v in nbr:
            dfsColor(graph, color, v, visited)
    return color


def findConnectedComponent(graph):
    visited = set()
    colorList = []

    for v in graph:
        if v not in visited:
            color = dfsColor(graph, [], v, visited)
            colorList.append(color)

    print(f"그래프 성분의 개수 : {len(colorList)}")
    print(colorList)

#  - test -
# myGraph = {'A': {'B', 'C'},
#            'B': {'A'},
#            'C': {'A'},
#            'D': {'E'},
#            'E': {'D'}}
#
# print("findConnectedComponent : ")
# findConnectedComponent(myGraph)
