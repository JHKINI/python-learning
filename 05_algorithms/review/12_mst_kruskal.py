# 최소 비용 신장 트리 - Kruskal 알고리즘
# coding: utf-8
parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a

def kruskal(vertices, edges):
    for v in vertices:
        parent[v] = v
    edges.sort(key=lambda x: x[2])
    mst = []
    total = 0
    for a, b, w in edges:
        if find(a) != find(b):
            union(a, b)
            mst.append((a, b, w))
            total += w
    return mst, total

V = ['A', 'B', 'C', 'D']
E = [('A','B',3), ('A','C',1), ('B','C',2), ('B','D',4), ('C','D',5)]
print(kruskal(V, E))
