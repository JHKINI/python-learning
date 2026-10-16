# 이진 트리 순회: 전위 / 중위 / 후위 / 레벨
# coding: utf-8
from collections import deque

class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(n):
    if n:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n):
    if n:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root):
    q = deque([root])
    while q:
        n = q.popleft()
        if n:
            print(n.data, end=' ')
            q.append(n.left)
            q.append(n.right)

root = TNode('A', TNode('B', TNode('D'), TNode('E')), TNode('C', None, TNode('F')))
print('전위:', end=' '); preorder(root); print()
print('중위:', end=' '); inorder(root); print()
print('후위:', end=' '); postorder(root); print()
print('레벨:', end=' '); levelorder(root); print()
