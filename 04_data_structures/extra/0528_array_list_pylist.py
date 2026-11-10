# -*- coding: utf-8 -*-
# 배열 구조 리스트 클래스 예제

class ArrayList:
    def __init__(self,capacity=10):
        self.items = []
        self.capacity = capacity

    # 삽입
    def insert(self, pos, item):
        self.items.insert(pos, item)

    # 삭제
    def delete(self, pos):
        return self.items.pop(pos)
    # 검사
    def isFull(self):
        return len(self.items) >= self.capacity

    # 항목 반환
    def getEntry(self, pos):
        return self.items[pos]

    # 리스트 크기
    def size(self):
        return len(self.items)
    #리스트 초기화
    def clear(self):
        self.items = []
    #찾아 바꾸기
    def find(self,item): 
        if item in self.items:
            return self.items.index(item) 
        return -1
    #항목변경
    def replace(self,pos,item):
        self.items[pos] = item
    #정렬
    def sort(self):
        self.items.sort() 
    #다른리스트 추가
    def merge(self,lst):
        self.items.extend(lst)   
    # 공백 검사
    def isEmpty(self):
        return len(self.items) == 0
    #맨뒤추가
    def append(self,item):
        self.items.append(item)

    # 전체 출력
    def display(self):
        print(self.items)


# =========================
# 인스턴스 생성 및 사용 예제
# =========================

lst = ArrayList()

lst.insert(0, "A")
lst.insert(1, "B")
lst.insert(2, "C")

print("리스트 출력:")
lst.display()

print("1번 위치 데이터:", lst.getEntry(1))

lst.delete(1)

print("삭제 후:")
lst.display()

print(lst.isFull())
print("리스트 크기:", lst.size())

lst.display()
lst.append("D")

print("현재 리스트:")
lst.display()

print("B 위치:", lst.find("B"))



print("변경 후:")
lst.display()

lst.sort()

print("정렬 후:")
lst.display()

lst.merge(["E", "F"])

print("합병 후:")
lst.display()

lst.clear()
print("초기화 후:")

print("공백 여부:", lst.isEmpty())