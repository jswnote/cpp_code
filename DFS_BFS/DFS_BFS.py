from collections import deque

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end = " ")

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
