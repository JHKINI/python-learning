pq = []

def enqueue(item):
    pq.append(item)

def dequeue():
    if len(pq) == 0:
        print("큐가 비어있음")
        return None
    
    max_idx = 0
    for i in range(1, len(pq)):
        if pq[i] > pq[max_idx]:
            max_idx = i

    return pq.pop(max_idx)


# 테스트
enqueue(3)
enqueue(1)
enqueue(5)
enqueue(2)

print("삭제:", dequeue())  # 5
print("삭제:", dequeue())  # 3
print("삭제:", dequeue())  # 2
print("삭제:", dequeue())  # 1