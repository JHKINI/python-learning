MAX_SIZE = 10
items = [None] * MAX_SIZE
size = 0


def isEmpty():
    return size == 0


def isFull():
    return size == MAX_SIZE


def contains(e):
    for i in range(size):
        if items[i] == e:
            return True
    return False


def insert(e):
    global size
    if isFull():
        print("가득 참")
        return
    if contains(e):
        print("중복 불가")
        return

    items[size] = e
    size += 1


def delete(e):
    global size
    for i in range(size):
        if items[i] == e:
            removed = items[i]

            for j in range(i, size - 1):
                items[j] = items[j + 1]

            items[size - 1] = None
            size -= 1
            return removed

    return None


def size_func():
    return size


def display():
    print(items[:size])


def union(setB):
    result = []
    for i in range(size):
        result.append(items[i])

    for e in setB:
        if e not in result:
            result.append(e)

    return result


def intersect(setB):
    result = []
    for i in range(size):
        if items[i] in setB:
            result.append(items[i])
    return result


def difference(setB):
    result = []
    for i in range(size):
        if items[i] not in setB:
            result.append(items[i])
    return result


def equals(setB):
    if size != len(setB):
        return False

    for i in range(size):
        if items[i] not in setB:
            return False

    return True