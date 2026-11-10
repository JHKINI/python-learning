# -*- coding: utf-8 -*-
# 예제: 이진탐색트리(BST) 탐색, 삽입, 삭제, 맵 구현
# key를 기준으로 왼쪽은 작은 값, 오른쪽은 큰 값을 저장

from collections import deque


class BSTNode:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def inorder(n):
    # 중위순회: BST에서는 오름차순 출력
    if n is not None:
        inorder(n.left)
        print(n.key, end=" ")
        inorder(n.right)


def levelorder(root):
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n is not None:
            print(n.key, end=" ")
            queue.append(n.left)
            queue.append(n.right)


def count_node(n):
    if n is None:
        return 0
    return 1 + count_node(n.left) + count_node(n.right)


def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)


def calc_height(n):
    if n is None:
        return 0
    return max(calc_height(n.left), calc_height(n.right)) + 1


def search_value_bst(n, value):
    # value 기준 탐색: 전체를 순회해야 하므로 느림
    if n is None:
        return None
    elif value == n.value:
        return n

    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)


def search_bst(n, key):
    # key 기준 재귀 탐색
    if n is None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)


def search_bst_iter(n, key):
    # key 기준 반복 탐색
    while n is not None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None


def search_max_bst(n):
    # 가장 큰 key는 가장 오른쪽에 있음
    while n is not None and n.right is not None:
        n = n.right
    return n


def search_min_bst(n):
    # 가장 작은 key는 가장 왼쪽에 있음
    while n is not None and n.left is not None:
        n = n.left
    return n


def insert_bst(r, n):
    # 탐색 실패 위치에 새 노드 삽입
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False


def delete_bst_case1(parent, node, root):
    # Case1: 삭제 노드가 단말 노드
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root


def delete_bst_case2(parent, node, root):
    # Case2: 삭제 노드의 자식이 하나
    if node.left is not None:
        child = node.left
    else:
        child = node.right

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root


def delete_bst_case3(parent, node, root):
    # Case3: 삭제 노드의 자식이 둘
    # 오른쪽 서브트리에서 가장 작은 후계 노드를 찾음
    succp = node
    succ = node.right

    while succ.left is not None:
        succp = succ
        succ = succ.left

    if succp.left == succ:
        succp.left = succ.right
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value
    node = succ
    return root


def delete_bst(root, key):
    # 삭제할 노드를 찾고 Case1~3 중 하나로 처리
    if root is None:
        return None

    parent = None
    node = root

    while node is not None and node.key != key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node is None:
        return root

    if node.left is None and node.right is None:
        root = delete_bst_case1(parent, node, root)
    elif node.left is None or node.right is None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)

    return root


class BSTMap:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def size(self):
        return count_node(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, value):
        return search_value_bst(self.root, value)

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg="BSTMap : "):
        print(msg, end="")
        inorder(self.root)
        print()


# 실행 예시
if __name__ == "__main__":
    map = BSTMap()
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

    print("[삽입연산] :", data)
    for key in data:
        map.insert(key)

    map.display("[중위순회] : ")

    if map.search(26) is not None:
        print("[탐색 26] : 성공")
    else:
        print("[탐색 26] : 실패")

    if map.search(25) is not None:
        print("[탐색 25] : 성공")
    else:
        print("[탐색 25] : 실패")

    map.delete(3)
    map.display("[3 삭제] : ")
    map.delete(68)
    map.display("[68 삭제] : ")
    map.delete(18)
    map.display("[18 삭제] : ")
    map.delete(35)
    map.display("[35 삭제] : ")
