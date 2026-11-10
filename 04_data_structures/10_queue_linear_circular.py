# =========================
# 1. 선형 큐 Linear Queue
# =========================

class LinearQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.front > self.rear

    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, data):
        if self.is_full():
            print("선형 큐 가득 참")
            return

        self.rear += 1
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("선형 큐 비어 있음")
            return None

        data = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        return data

    def show(self):
        print("LinearQueue:", self.queue)
        print("front:", self.front, "rear:", self.rear)


# =========================
# 2. 원형 큐 Circular Queue
# =========================

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, data):
        if self.is_full():
            print("원형 큐 가득 참")
            return

        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("원형 큐 비어 있음")
            return None

        data = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return data

    def show(self):
        print("CircularQueue:", self.queue)
        print("front:", self.front, "rear:", self.rear, "count:", self.count)


# =========================
# 활용 예제
# =========================

print("=== 선형 큐 예제 ===")
lq = LinearQueue(5)

lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
lq.enqueue(40)
lq.enqueue(50)
lq.show()

print("삭제:", lq.dequeue())
print("삭제:", lq.dequeue())
lq.show()

# 앞에 빈칸이 있어도 rear가 끝이라 추가 불가
lq.enqueue(60)
lq.show()


print("\n=== 원형 큐 예제 ===")
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.show()

print("삭제:", cq.dequeue())
print("삭제:", cq.dequeue())
cq.show()

# 앞에 빈칸을 다시 사용 가능
cq.enqueue(60)
cq.enqueue(70)
cq.show()