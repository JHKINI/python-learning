# -*- coding: utf-8 -*-
# 예제: 힙 구현 - 최대 힙(Max Heap)
# 가장 큰 값을 빠르게 꺼내는 완전이진트리 기반 자료구조


class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)  # 0번 인덱스는 사용하지 않음

    def size(self):
        return len(self.heap) - 1

    def isEmpty(self):
        return self.size() == 0

    def Parent(self, i):
        return self.heap[i // 2]

    def Left(self, i):
        return self.heap[i * 2]

    def Right(self, i):
        return self.heap[i * 2 + 1]

    def display(self, msg="힙트리: "):
        print(msg, self.heap[1:])

    def insert(self, n):
        # 삽입 후 부모와 비교하며 위로 올림
        self.heap.append(n)
        i = self.size()

        while i != 1 and n > self.Parent(i):
            self.heap[i] = self.Parent(i)
            i = i // 2

        self.heap[i] = n

    def delete(self):
        # 루트의 최댓값을 삭제하고 반환
        if self.isEmpty():
            return None

        parent = 1
        child = 2
        hroot = self.heap[1]
        last = self.heap[self.size()]

        while child <= self.size():
            if child < self.size() and self.heap[child] < self.heap[child + 1]:
                child += 1

            if last >= self.heap[child]:
                break

            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2

        self.heap[parent] = last
        self.heap.pop(-1)
        return hroot


# 실행 예시
if __name__ == "__main__":
    heap = MaxHeap()
    data = [2, 5, 4, 8, 9, 3, 7, 3]

    print("[삽입연산]:", data)
    for elem in data:
        heap.insert(elem)

    heap.display("[삽입후]: ")
    print("삭제값:", heap.delete())
    heap.display("[삭제후]: ")
    print("삭제값:", heap.delete())
    heap.display("[삭제후]: ")
