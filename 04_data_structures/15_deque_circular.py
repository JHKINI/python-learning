# 2. 원형 덱(Circular Deque)

class CircularDeque:

    # 생성자
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = 0
        self.rear = 0

    # 공백 상태 확인
    def is_empty(self):
        return self.front == self.rear

    # 포화 상태 확인
    def is_full(self):
        return self.front == (self.rear + 1) % self.size

    # 앞쪽 삽입
    def add_front(self, item):
        if self.is_full():
            print("덱이 가득 참")
        else:
            self.front = (self.front - 1) % self.size
            self.deque[self.front] = item

    # 뒤쪽 삽입
    def add_rear(self, item):
        if self.is_full():
            print("덱이 가득 참")
        else:
            self.deque[self.rear] = item
            self.rear = (self.rear + 1) % self.size

    # 앞쪽 삭제
    def delete_front(self):
        if self.is_empty():
            print("덱이 비어 있음")
        else:
            item = self.deque[self.front]
            self.deque[self.front] = None
            self.front = (self.front + 1) % self.size
            return item

    # 뒤쪽 삭제
    def delete_rear(self):
        if self.is_empty():
            print("덱이 비어 있음")
        else:
            self.rear = (self.rear - 1) % self.size
            item = self.deque[self.rear]
            self.deque[self.rear] = None
            return item

    # 앞쪽 데이터 확인
    def peek_front(self):
        if self.is_empty():
            return None
        return self.deque[self.front]

    # 뒤쪽 데이터 확인
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.deque[(self.rear - 1) % self.size]

    # 원형 덱 상태 출력
    def show(self):
        print(self.deque)
        print("front =", self.front, ", rear =", self.rear)


# -----------------------
# 테스트
# -----------------------

# 원형 덱은 한 칸을 비워두므로
# 크기 6이면 실제 저장 가능 원소는 5개
dq = CircularDeque(6)

print("뒤쪽에 10 삽입")
dq.add_rear(10)

print("뒤쪽에 20 삽입")
dq.add_rear(20)

print("앞쪽에 5 삽입")
dq.add_front(5)

print("현재 원형 덱")
dq.show()

print("앞쪽 원소:", dq.peek_front())
print("뒤쪽 원소:", dq.peek_rear())

print("앞쪽 삭제:", dq.delete_front())
print("뒤쪽 삭제:", dq.delete_rear())

print("삭제 후 원형 덱")
dq.show()

print("덱이 비어있는가?", dq.is_empty())
print("덱이 가득 찼는가?", dq.is_full())