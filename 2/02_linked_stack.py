# 연결된 스택 - 노드 이용
# coding: utf-8
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        if self.is_empty():
            print('스택이 비었습니다.')
            return None
        item = self.top.data
        self.top = self.top.link
        return item

    def peek(self):
        return None if self.is_empty() else self.top.data

    def display(self):
        cur = self.top
        print('TOP -> ', end='')
        while cur:
            print(cur.data, end=' -> ')
            cur = cur.link
        print('None')

s = LinkedStack()
s.push('A'); s.push('B'); s.push('C')
s.display()
print('pop:', s.pop())
s.display()
