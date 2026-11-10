class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def push(self, item):
        n = Node(item, self.top)
        self.top = n

    def pop(self):
        if self.is_empty():
            print("스택이 비어 있음")
            return None

        item = self.top.data
        self.top = self.top.link
        return item

    def peek(self):
        if self.is_empty():
            print("스택이 비어 있음")
            return None

        return self.top.data

    def size(self):
        count = 0
        n = self.top

        while n != None:
            count += 1
            n = n.link

        return count

    def clear(self):
        self.top = None

    def display(self):
        n = self.top
        print("스택:", end=' ')

        while n != None:
            print(n.data, end=' ')
            n = n.link

        print()


# 테스트
s = LinkedStack()

s.push('A')
s.push('B')
s.push('C')
s.display()

print("top:", s.peek())
print("pop:", s.pop())
s.display()

print("size:", s.size())