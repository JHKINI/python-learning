# -*- coding: utf-8 -*-
# 예제: 그래프 탐색 - DFS, BFS, 연결성분, 신장트리
# 인접리스트를 딕셔너리와 집합으로 표현

import collections


def dfs(graph, start, visited=None):
    # 깊이우선탐색: 한 방향으로 깊게 탐색
    if visited is None:
        visited = set()

    if start not in visited:
        visited.add(start)
        print(start, end=" ")
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)


def bfs(graph, start):
    # 너비우선탐색: 가까운 정점부터 탐색
    visited = set([start])
    queue = collections.deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        nbr = graph[vertex] - visited

        for v in nbr:
            visited.add(v)
            queue.append(v)


def dfs_cc(graph, color, vertex, visited):
    # 연결성분 하나 찾기
    if vertex not in visited:
        visited.add(vertex)
        color.append(vertex)
        nbr = graph[vertex] - visited

        for v in nbr:
            dfs_cc(graph, color, v, visited)

    return color


def find_connected_component(graph):
    # 그래프의 연결성분 찾기
    visited = set()
    colorList = []

    for vtx in graph:
        if vtx not in visited:
            color = dfs_cc(graph, [], vtx, visited)
            colorList.append(color)

    print("그래프 연결성분 개수 = %d" % len(colorList))
    print(colorList)


def bfsST(graph, start):
    # BFS 기반 신장트리 간선 출력
    visited = set([start])
    queue = collections.deque([start])

    while queue:
        v = queue.popleft()
        nbr = graph[v] - visited

        for u in nbr:
            print("(", v, ",", u, ") ", end="")
            visited.add(u)
            queue.append(u)


# 실행 예시
if __name__ == "__main__":
    graph = {
        "A": set(["B", "C"]),
        "B": set(["A", "D"]),
        "C": set(["A", "D"]),
        "D": set(["B", "C", "E"]),
        "E": set(["D"]),
    }

    print("DFS:", end=" ")
    dfs(graph, "A")
    print()

    print("BFS:", end=" ")
    bfs(graph, "A")
    print()

    mygraph = {
        "A": set(["B", "C"]),
        "B": set(["A"]),
        "C": set(["A"]),
        "D": set(["E"]),
        "E": set(["D"]),
    }

    find_connected_component(mygraph)

    print("BFS 신장트리:", end=" ")
    bfsST(graph, "A")
    print()
