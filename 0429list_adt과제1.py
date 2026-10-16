MAX_SIZE = 10
items = [None] * MAX_SIZE
size = 0


def isEmpty():
    return size == 0


def isFull():
    return size == MAX_SIZE


def append(e):
    global size
    if isFull():
        print("리스트가 가득 찼습니다.")
        return
    items[size] = e
    size += 1


def insert(pos, e):
    global size
    if isFull():
        print("리스트가 가득 찼습니다.")
        return
    if pos < 0 or pos > size:
        print("위치 오류")
        return

    # (간단 shift - 최소 구현)
    for i in range(size, pos, -1):
        items[i] = items[i - 1]

    items[pos] = e
    size += 1


def delete(pos):
    global size
    if isEmpty():
        print("비어있음")
        return None
    if pos < 0 or pos >= size:
        print("위치 오류")
        return None

    removed = items[pos]

    for i in range(pos, size - 1):
        items[i] = items[i + 1]

    items[size - 1] = None
    size -= 1

    return removed


def getEntry(pos):
    if pos < 0 or pos >= size:
        print("위치 오류")
        return None
    return items[pos]


def size_func():
    return size


def clear():
    global size
    for i in range(size):
        items[i] = None
    size = 0


def find(item):
    for i in range(size):
        if items[i] == item:
            return i
    return -1


def replace(pos, item):
    if pos < 0 or pos >= size:
        print("위치 오류")
        return
    items[pos] = item


def sort():
    valid = items[:size]
    valid.sort()
    for i in range(size):
        items[i] = valid[i]


def merge(lst):
    global size
    if size + len(lst) > MAX_SIZE:
        print("초과")
        return
    for e in lst:
        append(e)


def display():
    print(items[:size])