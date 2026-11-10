# -*- coding: utf-8 -*-
# 연결된 구조 리스트(단순 연결 리스트) 클래스 예제

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    # 삽입: pos 위치에 item 삽입
    def insert(self, pos, item):
        new_node = Node(item)

        if pos == 0:
            new_node.link = self.head
            self.head = new_node
            return

        prev = self.head
        for i in range(pos - 1):
            if prev is None:
                return
            prev = prev.link

        if prev is None:
            return

        new_node.link = prev.link
        prev.link = new_node

    # 삭제: pos 위치 삭제
    def delete(self, pos):
        if self.head is None:
            return None

        if pos == 0:
            deleted = self.head
            self.head = self.head.link
            return deleted.data

        prev = self.head
        for i in range(pos - 1):
            if prev.link is None:
                return None
            prev = prev.link

        deleted = prev.link
        if deleted is None:
            return None

        prev.link = deleted.link
        return deleted.data

    # 항목 반환
    def getEntry(self, pos):
        node = self.head
        for i in range(pos):
            if node is None:
                return None
            node = node.link

        if node is None:
            return None
        return node.data

    # 리스트 크기
    def size(self):
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.link

        return count

    # 리스트 초기화
    def clear(self):
        self.head = None

    # 찾기
    def find(self, item):
        node = self.head
        index = 0

        while node is not None:
            if node.data == item:
                return index
            node = node.link
            index += 1

        return -1

    # 항목 변경
    def replace(self, pos, item):
        node = self.head
        for i in range(pos):
            if node is None:
                return
            node = node.link

        if node is not None:
            node.data = item

    # 정렬
    def sort(self):
        data_list = []

        node = self.head
        while node is not None:
            data_list.append(node.data)
            node = node.link

        data_list.sort()

        self.clear()

        for item in reversed(data_list):
            self.insert(0, item)

    # 다른 리스트 추가
    def merge(self, lst):
        for item in lst:
            self.append(item)

    # 공백 검사
    def isEmpty(self):
        return self.head is None

    # 맨 뒤 추가
    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return

        node = self.head
        while node.link is not None:
            node = node.link

        node.link = new_node

    # 전체 출력
    def display(self):
        node = self.head

        while node is not None:
            print(node.data, end=" -> ")
            node = node.link

        print("None")


# =========================
# 인스턴스 생성 및 사용 예제
# =========================

slist = LinkedList()

slist.insert(0, "A")
slist.insert(1, "B")
slist.insert(2, "C")

print("연결 리스트 출력:")
slist.display()

print("1번 위치 데이터:", slist.getEntry(1))

slist.delete(1)

print("삭제 후:")
slist.display()

print("리스트 크기:", slist.size())

slist.append("D")

print("현재 리스트:")
slist.display()

print("B 위치:", slist.find("B"))

slist.replace(1, "X")

print("변경 후:")
slist.display()

slist.sort()

print("정렬 후:")
slist.display()

slist.merge(["E", "F"])

print("합병 후:")
slist.display()

slist.clear()

print("초기화 후:")
slist.display()

print("공백 여부:", slist.isEmpty())