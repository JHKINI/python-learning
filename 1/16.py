# -*- coding: utf-8 -*-
# 예제: 최단경로 - Dijkstra 알고리즘
# 시작 정점에서 다른 모든 정점까지의 최단경로 찾기

INF = 9999


def choose_vertex(dist, found):
    # 아직 확정되지 않은 정점 중 dist가 가장 작은 정점 선택
    min_value = INF
    minpos = -1

    for i in range(len(dist)):
        if dist[i] < min_value and found[i] is False:
            min_value = dist[i]
            minpos = i

    return minpos


def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    path = [start] * vsize
    found = [False] * vsize

    found[start] = True
    dist[start] = 0

    for i in range(vsize):
        print("Step%2d: " % (i + 1), dist)
        u = choose_vertex(dist, found)

        if u == -1:
            break

        found[u] = True

        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return path


# 실행 예시
if __name__ == "__main__":
    vertex = ["A", "B", "C", "D", "E", "F", "G"]
    weight = [
        [0, 7, INF, INF, 3, 10, INF],
        [7, 0, 4, 10, 2, 6, INF],
        [INF, 4, 0, 2, INF, INF, INF],
        [INF, 10, 2, 0, 11, 9, 4],
        [3, 2, INF, 11, 0, 13, 5],
        [10, 6, INF, 9, 13, 0, INF],
        [INF, INF, INF, 4, 5, INF, 0],
    ]

    print("Shortest Path By Dijkstra Algorithm")
    start = 0
    path = shortest_path_dijkstra(vertex, weight, start)

    for end in range(len(vertex)):
        if end != start:
            print("[최단경로: %s->%s] %s" % (vertex[start], vertex[end], vertex[end]), end="")
            now = end
            while path[now] != start:
                print(" <- %s" % vertex[path[now]], end="")
                now = path[now]
            print(" <- %s" % vertex[path[now]])
