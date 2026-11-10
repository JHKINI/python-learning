# 1. 선형 덱(Linear Deque)

class LinearDeque:

    # 생성자
    def __init__(self, size):
        self.size = size          # 최대 크기
        self.deque = []           # 덱 저장용 리스트

    # 공백 상태 확인
    def is_empty(self):
        return len(self.deque) == 0

    # 포화 상태 확인
    def is_full(self):
        return len(self.deque) == self.size

    # 앞쪽 삽입
    def add_front(self, item):
        if self.is_full():
            print("덱이 가득 참")
        else:
            self.deque.insert(0, item)

    # 뒤쪽 삽입
    def add_rear(self, item):
        if self.is_full():
            print("덱이 가득 참")
        else:
            self.deque.append(item)

    # 앞쪽 삭제
    def delete_front(self):
        if self.is_empty():
            print("덱이 비어 있음")
        else:
            return self.deque.pop(0)

    # 뒤쪽 삭제
    def delete_rear(self):
        if self.is_empty():
            print("덱이 비어 있음")
        else:
            return self.deque.pop()

    # 앞쪽 데이터 확인
    def peek_front(self):
        if self.is_empty():
            return None
        return self.deque[0]

    # 뒤쪽 데이터 확인
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.deque[-1]

    # 덱 출력
    def show(self):
        print(self.deque)


# -----------------------
# 테스트
# -----------------------

dq = LinearDeque(5)

print("뒤쪽에 10 삽입")
dq.add_rear(10)

print("뒤쪽에 20 삽입")
dq.add_rear(20)

print("앞쪽에 5 삽입")
dq.add_front(5)

print("현재 덱")
dq.show()

print("앞쪽 원소:", dq.peek_front())
print("뒤쪽 원소:", dq.peek_rear())

print("앞쪽 삭제:", dq.delete_front())
print("뒤쪽 삭제:", dq.delete_rear())

print("삭제 후 덱")
dq.show()

print("덱이 비어있는가?", dq.is_empty())
print("덱이 가득 찼는가?", dq.is_full())