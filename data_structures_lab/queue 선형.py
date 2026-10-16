
# 1. 선형 큐 Linear Queue


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


# 활용 예제


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
