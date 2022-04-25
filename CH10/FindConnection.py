def findConnection(graph):
    visited = {}
    colorList = []

    for vtx in graph:
        if vtx not in visited:
            color = dfsCC(graph, [], vtx, visited)
            colorList.append(color)

    print(f"그래프 연결성분 개수 = {len(colorList)}")
    print(colorList)

def dfsCC(graph, color, vertex, visited):
    if vertex not in visited:
        visited.add(vertex)
        color.append(vertex)
        nbr = graph[vertex] - visited
        for v in nbr:
            dfsCC(graph, color, v, visited)

    return color