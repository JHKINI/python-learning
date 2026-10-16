# -*- coding: utf-8 -*-
# 예제: 최소비용 신장트리 - Kruskal 알고리즘
# 간선을 가중치 오름차순으로 선택하고, Union-Find로 사이클을 검사


parent = []
set_size = 0


def init_set(nSets):
    global set_size, parent
    set_size = nSets
    parent = []
    for i in range(nSets):
        parent.append(-1)


def find(id):
    # 원소가 속한 집합의 대표 찾기
    while parent[id] >= 0:
        id = parent[id]
    return id


def union(s1, s2):
    # 두 집합 합치기
    global set_size
    parent[s1] = s2
    set_size = set_size - 1


def MSTKruskal(vertex, adj):
    vsize = len(vertex)
    init_set(vsize)
    eList = []

    # 모든 간선 목록 만들기
    for i in range(vsize - 1):
        for j in range(i + 1, vsize):
            if adj[i][j] is not None:
                eList.append((i, j, adj[i][j]))

    # 가중치 기준 정렬
    eList.sort(key=lambda e: e[2], reverse=True)

    edgeAccepted = 0
    while edgeAccepted < vsize - 1:
        e = eList.pop(-1)
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset:
            print("간선추가: (%s, %s, %d)" % (vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)
            edgeAccepted += 1


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

    print("MST By Kruskal's Algorithm")
    MSTKruskal(vertex, weight)
