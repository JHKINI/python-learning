# 이진 탐색 트리 기반 맵
# coding: utf-8
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTMap:
    def __init__(self):
        self.root = None

    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:
                return cur.value
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        return node

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f'{node.key}:{node.value}', end=' ')
            self._inorder(node.right)

m = BSTMap()
m.insert(30, 'A'); m.insert(10, 'B'); m.insert(40, 'C'); m.insert(20, 'D')
m.inorder()
print('20 검색:', m.search(20))
