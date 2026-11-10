# -*- coding: utf-8 -*-
# 예제: 최소비용 신장트리 - Prim 알고리즘
# 하나의 정점에서 시작해 가장 가까운 정점을 하나씩 선택

INF = 9999


def getMinVertex(dist, selected):
    # 아직 선택되지 않은 정점 중 dist가 가장 작은 정점 찾기
    minv = 0
    mindist = INF

    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v

    return minv


def MSTPrim(vertex, adj):
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0

    for i in range(vsize):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=" ")

        for v in range(vsize):
            if adj[u][v] is not None:
                if selected[v] is False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]
    print()


# 실행 예시
if __name__ == "__main__":
    vertex = ["A", "B", "C", "D", "E", "F", "G"]
    weight = [
        [None, 29, None, None, None, 10, None],
        [29, None, 16, None, None, None, 15],
        [None, 16, None, 12, None, None, None],
        [None, None, 12, None, 22, None, 18],
        [None, None, None, 22, None, 27, 25],
        [10, None, None, None, 27, None, None],
        [None, 15, None, 18, 25, None, None],
    ]

    print("MST By Prim's Algorithm")
    MSTPrim(vertex, weight)
