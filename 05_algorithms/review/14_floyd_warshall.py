# 모든 정점 사이 최단 경로 - Floyd-Warshall
# coding: utf-8
INF = 9999

A = [
    [0,   5, INF, 8],
    [7,   0,   9, INF],
    [2, INF,   0,   4],
    [INF, INF, 3,   0]
]

def floyd_warshall(dist):
    n = len(dist)
    dist = [row[:] for row in dist]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

for row in floyd_warshall(A):
    print(row)
