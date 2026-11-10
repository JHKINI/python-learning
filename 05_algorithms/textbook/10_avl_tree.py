# -*- coding: utf-8 -*-
# 예제: AVL 트리 - 균형 이진탐색트리
# 삽입 후 트리 균형이 깨지면 LL, RR, LR, RL 회전으로 재균형

from collections import deque


class BSTNode:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1


def calc_height_diff(n):
    if n is None:
        return 0
    return calc_height(n.left) - calc_height(n.right)


def rotateLL(A):
    # LL 회전: 시계방향 회전
    B = A.left
    A.left = B.right
    B.right = A
    return B


def rotateRR(A):
    # RR 회전: 반시계방향 회전
    B = A.right
    A.right = B.left
    B.left = A
    return B


def rotateRL(A):
    # RL 회전: 오른쪽 자식에 LL 후, 현재 노드에 RR
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)


def rotateLR(A):
    # LR 회전: 왼쪽 자식에 RR 후, 현재 노드에 LL
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)


def reBalance(parent):
    # 균형인수에 따라 회전 선택
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)

    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)

    return parent


def insert_avl(parent, node):
    # BST 방식으로 삽입 후 재균형
    if node.key < parent.key:
        if parent.left is not None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key:
        if parent.right is not None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)

    else:
        print("중복된 키 에러")
        return parent


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


class AVLMap:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root, n)

    def display(self, msg="AVLMap : "):
        print(msg, end="")
        levelorder(self.root)
        print()


# 실행 예시
if __name__ == "__main__":
    node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    map = AVLMap()

    for i in node:
        map.insert(i)
        map.display("AVL(%d): " % i)

    print("노드의 개수 = %d" % count_node(map.root))
    print("단말의 개수 = %d" % count_leaf(map.root))
    print("트리의 높이 = %d" % calc_height(map.root))
