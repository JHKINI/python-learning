# -*- coding: utf-8 -*-
# 선형 우선순위 큐 ADT 구현

class PriorityQueueADT:

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.data = []

    # 공백 검사
    def isEmpty(self):
        return len(self.data) == 0

    # 포화 검사
    def isFull(self):
        return len(self.data) == self.max_size

    # Enqueue(e): 원소 삽입
    def enqueue(self, e):
        if self.isFull():
            print("우선순위 큐가 가득 참")
            return

        self.data.append(e)

    # Dequeue(): 가장 우선순위가 높은 원소 삭제 후 반환
    def dequeue(self):
        if self.isEmpty():
            print("우선순위 큐가 비어 있음")
            return None

        max_idx = 0

        for i in range(1, len(self.data)):
            if self.data[i] > self.data[max_idx]:
                max_idx = i

        return self.data.pop(max_idx)

    # Peek(): 가장 우선순위가 높은 원소 확인
    def peek(self):
        if self.isEmpty():
            print("우선순위 큐가 비어 있음")
            return None

        max_idx = 0

        for i in range(1, len(self.data)):
            if self.data[i] > self.data[max_idx]:
                max_idx = i

        return self.data[max_idx]

    # Size(): 원소 개수 반환
    def size(self):
        return len(self.data)

    # Clear(): 모든 원소 삭제
    def clear(self):
        self.data = []

    # 출력
    def display(self):
        print(self.data)


# 테스트

pq = PriorityQueueADT(5)

pq.enqueue(3)
pq.enqueue(1)
pq.enqueue(5)
pq.enqueue(2)

print("현재 우선순위 큐:")
pq.display()

print("가장 우선순위 높은 원소:", pq.peek())

print("큐 크기:", pq.size())

print("삭제:", pq.dequeue())
print("삭제:", pq.dequeue())
print("삭제:", pq.dequeue())
print("삭제:", pq.dequeue())

print("삭제 후 큐:")
pq.display()

print("비어있는가?", pq.isEmpty())

pq.clear()
print("초기화 후:")
pq.display()