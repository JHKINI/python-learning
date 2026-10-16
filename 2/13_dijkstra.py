# 최단 경로 - Dijkstra 알고리즘
# coding: utf-8
INF = 9999

vertex = ['A', 'B', 'C', 'D', 'E']
weight = [
    [0,   7,   4, INF, INF],
    [7,   0,   2,   5, INF],
    [4,   2,   0,   1,   8],
    [INF, 5,   1,   0,   3],
    [INF, INF, 8,   3,   0]
]

def choose_vertex(dist, found):
    min_dist = INF
    min_pos = -1
    for i in range(len(dist)):
        if not found[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_pos = i
    return min_pos

def dijkstra(start):
    n = len(vertex)
    dist = weight[start][:]
    found = [False] * n
    found[start] = True
    dist[start] = 0

    for _ in range(n - 1):
        u = choose_vertex(dist, found)
        if u == -1:
            break
        found[u] = True
        for w in range(n):
            if not found[w] and dist[u] + weight[u][w] < dist[w]:
                dist[w] = dist[u] + weight[u][w]
    return dist

print('A에서 각 정점까지:', dijkstra(0))
