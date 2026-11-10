# -*- coding: utf-8 -*-
# 배열 기반 StackADT 구현

class StackADT:

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.items = [None] * max_size
        self.top = -1

    # 공백 검사
    def isEmpty(self):
        return self.top == -1

    # 포화 검사
    def isFull(self):
        return self.top == self.max_size - 1

    # Push(e)
    def push(self, e):
        if self.isFull():
            print("스택이 가득 참")
            return

        self.top += 1
        self.items[self.top] = e

    # Pop()
    def pop(self):
        if self.isEmpty():
            print("스택이 비어 있음")
            return None

        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    # Peek()
    def peek(self):
        if self.isEmpty():
            return None

        return self.items[self.top]

    # Size()
    def size(self):
        return self.top + 1

    # Clear()
    def clear(self):
        self.items = [None] * self.max_size
        self.top = -1

    # 출력용
    def display(self):
        print(self.items[:self.top + 1])

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