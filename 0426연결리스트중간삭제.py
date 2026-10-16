class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert(self, pos, item):
        new_node = Node(item)

        if pos == 0:
            new_node.link = self.head
            self.head = new_node
            return

        prev = self.head
        for _ in range(pos - 1):
            prev = prev.link

        new_node.link = prev.link
        prev.link = new_node

    def delete(self, pos):
        if self.is_empty():
            print("리스트 비어 있음")
            return None

        if pos == 0:
            removed = self.head
            self.head = self.head.link
            return removed.data

        prev = self.head
        for _ in range(pos - 1):
            prev = prev.link

        removed = prev.link
        prev.link = removed.link
        return removed.data

    def get_entry(self, pos):
        n = self.head
        for _ in range(pos):
            n = n.link
        return n.data

    def size(self):
        count = 0
        n = self.head
        while n != None:
            count += 1
            n = n.link
        return count

    def find(self, item):
        n = self.head
        idx = 0
        while n != None:
            if n.data == item:
                return idx
            n = n.link
            idx += 1
        return -1

    def display(self):
        n = self.head
        print("리스트:", end=' ')
        while n != None:
            print(n.data, end=' -> ')
            n = n.link
        print("None")


# 테스트
lst = LinkedList()

lst.insert(0, 'A')
lst.insert(1, 'B')
lst.insert(2, 'C')
lst.insert(1, 'D')

lst.display()

print("삭제:", lst.delete(2))
lst.display()

print("찾기 B:", lst.find('B'))
print("크기:", lst.size())