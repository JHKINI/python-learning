# 그래프 DFS / BFS - 인접 리스트 기반
# coding: utf-8
from collections import deque

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for v in graph[start] - visited:
        dfs(graph, v, visited)

def bfs(graph, start):
    visited = {start}
    q = deque([start])
    while q:
        v = q.popleft()
        print(v, end=' ')
        for nxt in graph[v] - visited:
            visited.add(nxt)
            q.append(nxt)

print('DFS:', end=' '); dfs(graph, 'A'); print()
print('BFS:', end=' '); bfs(graph, 'A'); print()
