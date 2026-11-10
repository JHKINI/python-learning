from collections import deque

dq = deque()

# ------------------
# 1. 큐처럼 사용 (FIFO)
# ------------------
dq.append(1)   # 뒤에 넣기
dq.append(2)
dq.append(3)

print("큐:", dq)

print("큐 삭제:", dq.popleft())  # 앞에서 꺼냄
print("큐 상태:", dq)


# ------------------
# 2. 스택처럼 사용 (LIFO)
# ------------------
dq.append(4)
dq.append(5)

print("스택:", dq)

print("스택 삭제:", dq.pop())  # 뒤에서 꺼냄
print("스택 상태:", dq)