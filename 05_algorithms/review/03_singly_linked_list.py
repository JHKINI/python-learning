# 단순 연결 리스트
# coding: utf-8
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, item):
        self.head = Node(item, self.head)

    def insert_last(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            return
        cur = self.head
        while cur.link:
            cur = cur.link
        cur.link = new_node

    def delete_first(self):
        if self.is_empty():
            return None
        item = self.head.data
        self.head = self.head.link
        return item

    def search(self, item):
        cur = self.head
        while cur:
            if cur.data == item:
                return True
            cur = cur.link
        return False

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=' -> ')
            cur = cur.link
        print('None')

lst = LinkedList()
lst.insert_last(10); lst.insert_last(20); lst.insert_first(5)
lst.display()
print('20 있음?', lst.search(20))
print('삭제:', lst.delete_first())
lst.display()
