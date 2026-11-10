MAX_SIZE = 10
deque = [None] * MAX_SIZE

front = 0
rear = 0


def is_empty():
    return front == rear


def is_full():
    return front == (rear + 1) % MAX_SIZE


def add_rear(item):
    global rear
    if is_full():
        print("덱이 가득 참")
        return
    rear = (rear + 1) % MAX_SIZE
    deque[rear] = item


def add_front(item):
    global front
    if is_full():
        print("덱이 가득 참")
        return
    deque[front] = item
    front = (front - 1 + MAX_SIZE) % MAX_SIZE


def delete_front():
    global front
    if is_empty():
        print("덱이 비어 있음")
        return None
    front = (front + 1) % MAX_SIZE
    return deque[front]


def delete_rear():
    global rear
    if is_empty():
        print("덱이 비어 있음")
        return None
    item = deque[rear]
    rear = (rear - 1 + MAX_SIZE) % MAX_SIZE
    return item


def get_front():
    if is_empty():
        return None
    return deque[(front + 1) % MAX_SIZE]


def get_rear():
    if is_empty():
        return None
    return deque[rear]


def display():
    print("덱 상태:", end=' ')
    i = (front + 1) % MAX_SIZE
    while i != (rear + 1) % MAX_SIZE:
        print(deque[i], end=' ')
        i = (i + 1) % MAX_SIZE
    print()


# 테스트
add_rear(1)
add_rear(2)
add_front(0)
display()

print("front 삭제:", delete_front())
print("rear 삭제:", delete_rear())
display()