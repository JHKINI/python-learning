# 위상 정렬 - 방향 그래프
# coding: utf-8
from collections import deque

vertex = ['A', 'B', 'C', 'D', 'E', 'F']
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

def topological_sort(graph):
    indegree = {v: 0 for v in graph}
    for v in graph:
        for nxt in graph[v]:
            indegree[nxt] += 1

    q = deque([v for v in graph if indegree[v] == 0])
    result = []
    while q:
        v = q.popleft()
        result.append(v)
        for nxt in graph[v]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    return result

print(topological_sort(graph))
