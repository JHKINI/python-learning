# -*- coding: utf-8 -*-
# 연결 구조 기반 StackADT 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class StackADT:

    def __init__(self):
        self.top = None
        self.count = 0

    # 공백 검사
    def isEmpty(self):
        return self.top is None

    # 포화 검사
    def isFull(self):
        return False

    # Push(e)
    def push(self, e):
        new_node = Node(e)

        new_node.link = self.top
        self.top = new_node

        self.count += 1

    # Pop()
    def pop(self):
        if self.isEmpty():
            print("스택이 비어 있음")
            return None

        item = self.top.data
        self.top = self.top.link

        self.count -= 1

        return item

    # Peek()
    def peek(self):
        if self.isEmpty():
            return None

        return self.top.data

    # Size()
    def size(self):
        return self.count

    # Clear()
    def clear(self):
        self.top = None
        self.count = 0

    # 출력
    def display(self):

        current = self.top
        result = []

        while current is not None:
            result.append(current.data)
            current = current.link

        print(result)


# 테스트

stack = StackADT()

print("비어있는가?", stack.isEmpty())

stack.push("A")
stack.push("B")
stack.push("C")

print("현재 스택")
stack.display()

print("맨 위 원소:", stack.peek())

print("스택 크기:", stack.size())

print("Pop:", stack.pop())

print("삭제 후")
stack.display()

print("맨 위 원소:", stack.peek())

print("스택 크기:", stack.size())

print("가득 찼는가?", stack.isFull())

stack.clear()

print("초기화 후")
stack.display()

print("비어있는가?", stack.isEmpty())