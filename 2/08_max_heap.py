# 최대 힙 구현
# coding: utf-8
class MaxHeap:
    def __init__(self):
        self.heap = [None]  # 1번 인덱스부터 사용

    def insert(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1
        while i > 1:
            parent = i // 2
            if self.heap[parent] >= item:
                break
            self.heap[i] = self.heap[parent]
            i = parent
        self.heap[i] = item

    def delete(self):
        if len(self.heap) == 1:
            return None
        root = self.heap[1]
        last = self.heap.pop()
        if len(self.heap) == 1:
            return root
        i = 1
        while i * 2 < len(self.heap):
            child = i * 2
            if child + 1 < len(self.heap) and self.heap[child] < self.heap[child + 1]:
                child += 1
            if last >= self.heap[child]:
                break
            self.heap[i] = self.heap[child]
            i = child
        self.heap[i] = last
        return root

h = MaxHeap()
for x in [2, 5, 4, 8, 9, 3]:
    h.insert(x)
print(h.heap)
print('삭제:', h.delete())
print(h.heap)
