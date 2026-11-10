# -*- coding: utf-8 -*-
# 배열 기반 ListADT 구현

class ListADT:

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.items = [None] * max_size
        self.size = 0

    # 공백 검사
    def isEmpty(self):
        return self.size == 0

    # 포화 검사
    def isFull(self):
        return self.size == self.max_size

    # 삽입
    def insert(self, pos, item):
        if self.isFull():
            print("리스트가 가득 참")
            return

        if pos < 0 or pos > self.size:
            print("삽입 위치 오류")
            return

        for i in range(self.size, pos, -1):
            self.items[i] = self.items[i - 1]

        self.items[pos] = item
        self.size += 1

    # 삭제
    def delete(self, pos):
        if self.isEmpty():
            print("리스트가 비어 있음")
            return None

        if pos < 0 or pos >= self.size:
            print("삭제 위치 오류")
            return None

        removed = self.items[pos]

        for i in range(pos, self.size - 1):
            self.items[i] = self.items[i + 1]

        self.items[self.size - 1] = None
        self.size -= 1

        return removed

    # 항목 반환
    def getEntry(self, pos):
        if pos < 0 or pos >= self.size:
            return None
        return self.items[pos]

    # 리스트 초기화
    def clear(self):
        self.items = [None] * self.max_size
        self.size = 0

    # 탐색
    def find(self, item):
        for i in range(self.size):
            if self.items[i] == item:
                return i
        return -1

    # 항목 변경
    def replace(self, pos, item):
        if pos < 0 or pos >= self.size:
            return
        self.items[pos] = item

    # 맨 뒤 추가
    def append(self, item):
        self.insert(self.size, item)

    # 현재 크기
    def size_func(self):
        return self.size

    # 출력
    def display(self):
        print(self.items[:self.size])


lst = ListADT()

lst.insert(0, "A")
lst.insert(1, "B")
lst.insert(2, "C")

print("현재 리스트")
lst.display()

print("1번 위치:", lst.getEntry(1))

lst.delete(1)

print("삭제 후")
lst.display()

print("B 위치:", lst.find("B"))

lst.append("D")

print("추가 후")
lst.display()

lst.replace(1, "X")

print("변경 후")
lst.display()

print("크기:", lst.size_func())

print("비어있는가?", lst.isEmpty())

lst.clear()

print("초기화 후")
lst.display()

print("비어있는가?", lst.isEmpty())