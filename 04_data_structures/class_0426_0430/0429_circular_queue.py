MAX_QSIZE = 8

queue = [None] * MAX_QSIZE
front = 0
rear = 0


def is_empty():
    return front == rear


def is_full():
    return front == (rear + 1) % MAX_QSIZE


def enqueue(item):
    global rear

    if is_full():
        print("큐가 포화상태입니다.")
        return

    rear = (rear + 1) % MAX_QSIZE
    queue[rear] = item


def dequeue():
    global front

    if is_empty():
        print("큐가 공백상태입니다.")
        return None

    front = (front + 1) % MAX_QSIZE
    return queue[front]


def peek():
    if is_empty():
        print("큐가 공백상태입니다.")
        return None

    return queue[(front + 1) % MAX_QSIZE]


def display():
    print("front =", front, "rear =", rear)
    i = (front + 1) % MAX_QSIZE

    while i != (rear + 1) % MAX_QSIZE:
        print(queue[i], end=" ")
        i = (i + 1) % MAX_QSIZE

    print()


enqueue('A')
enqueue('B')
enqueue('C')
enqueue('D')
display()

print("삭제:", dequeue())
print("삭제:", dequeue())
display()

enqueue('E')
enqueue('F')
enqueue('G')
display()