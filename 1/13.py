# -*- coding: utf-8 -*-
# 예제: 가중치 그래프 표현
# 인접행렬과 인접리스트로 간선 가중치 합과 전체 간선 출력


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


def weightSum_AM(vlist, W):
    # 인접행렬 기반 가중치 합
    total = 0
    for i in range(len(vlist)):
        for j in range(i + 1, len(vlist)):
            if W[i][j] is not None:
                total += W[i][j]
    return total


def printAllEdges_AM(vlist, W):
    # 인접행렬 기반 전체 간선 출력
    for i in range(len(vlist)):
        for j in range(i + 1, len(W[i])):
            if W[i][j] is not None and W[i][j] != 0:
                print("(%s,%s,%d)" % (vlist[i], vlist[j], W[i][j]), end=" ")
    print()


graphAL = {
    "A": set([("B", 29), ("F", 10)]),
    "B": set([("A", 29), ("C", 16), ("G", 15)]),
    "C": set([("B", 16), ("D", 12)]),
    "D": set([("C", 12), ("E", 22), ("G", 18)]),
    "E": set([("D", 22), ("F", 27), ("G", 25)]),
    "F": set([("A", 10), ("E", 27)]),
    "G": set([("B", 15), ("D", 18), ("E", 25)]),
}


def weightSum_AL(graph):
    # 인접리스트 기반 가중치 합
    total = 0
    for v in graph:
        for e in graph[v]:
            total += e[1]
    return total // 2


def printAllEdges_AL(graph):
    # 인접리스트 기반 전체 간선 출력
    for v in graph:
        for e in graph[v]:
            print("(%s,%s,%d)" % (v, e[0], e[1]), end=" ")
    print()


# 실행 예시
if __name__ == "__main__":
    print("AM : weight sum =", weightSum_AM(vertex, weight))
    printAllEdges_AM(vertex, weight)

    print("AL : weight sum =", weightSum_AL(graphAL))
    printAllEdges_AL(graphAL)
