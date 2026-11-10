# -*- coding: utf-8 -*-
# 예제: 이진트리 순회와 기본 연산
# 87페이지 트리 단원 이후 - 전위/중위/후위/레벨 순회, 노드 개수, 단말 개수, 트리 높이

from collections import deque


class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(n):
    # 전위순회: 루트 -> 왼쪽 -> 오른쪽
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)


def inorder(n):
    # 중위순회: 왼쪽 -> 루트 -> 오른쪽
    if n is not None:
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)


def postorder(n):
    # 후위순회: 왼쪽 -> 오른쪽 -> 루트
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=" ")


def levelorder(root):
    # 레벨순회: 위 레벨부터 차례대로 방문
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n is not None:
            print(n.data, end=" ")
            queue.append(n.left)
            queue.append(n.right)


def count_node(n):
    # 전체 노드 개수
    if n is None:
        return 0
    return 1 + count_node(n.left) + count_node(n.right)


def count_leaf(n):
    # 단말 노드 개수: 자식이 없는 노드
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)


def calc_height(n):
    # 트리 높이 계산
    if n is None:
        return 0

    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)

    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1


# 실행 예시
if __name__ == "__main__":
    d = TNode("D")
    e = TNode("E")
    b = TNode("B", d, e)
    f = TNode("F")
    c = TNode("C", f, None)
    root = TNode("A", b, c)

    print("In-Order : ", end="")
    inorder(root)
    print("\nPre-Order : ", end="")
    preorder(root)
    print("\nPost-Order : ", end="")
    postorder(root)
    print("\nLevel-Order : ", end="")
    levelorder(root)
    print()

    print("노드의 개수 = %d개" % count_node(root))
    print("단말의 개수 = %d개" % count_leaf(root))
    print("트리의 높이 = %d" % calc_height(root))
