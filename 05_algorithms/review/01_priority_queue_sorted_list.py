# 우선순위 큐 - 정렬된 리스트 이용
# 숫자가 작을수록 우선순위가 높다고 가정
# coding: utf-8
class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        self.items.sort()      # 항상 우선순위 순서 유지

    def dequeue(self):
        if self.is_empty():
            print('우선순위 큐가 비었습니다.')
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def display(self):
        print('PQ:', self.items)

pq = PriorityQueue()
for x in [30, 10, 50, 20]:
    pq.enqueue(x)
pq.display()
print('삭제:', pq.dequeue())
pq.display()
